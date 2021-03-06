#include "Gridded.h"

const float Gridded::eval (const Vector &p) const 
{
	//Return the trilinear result of P in grid
	Vec3f pos(p.X(), p.Y(), p.Z());
	
	//Create a sampler
	openvdb::tools::GridSampler<FloatGrid, openvdb::tools::BoxSampler> sampler(*grid);
	
	return sampler.wsSample(pos);
}

const float VDB_Gridded::eval (const Vector &p) const 
{
	//Return the trilinear result of P in grid
	Vec3f pos(p.X(), p.Y(), p.Z());
	
	//Create a sampler
	openvdb::tools::GridSampler<FloatGrid, openvdb::tools::BoxSampler> sampler(*grid);
	
	return -sampler.wsSample(pos);
}

const Color Gridded_Color::eval (const Vector &p) const 
{
	//Return the trilinear result of P in grid
	Vec3f pos(p.X(), p.Y(), p.Z());
	float r, g, b, a;
	//Create a sampler
	openvdb::tools::GridSampler<Vec4fGrid, openvdb::tools::BoxSampler> sampler(*grid);
	
	//Get RGBA from color grid
	Vec4s v4 = sampler.wsSample(pos);
	r = v4.x();
	g = v4.y();
	b = v4.z();
	a = v4.w();
	
	Color grid_color(r, g, b, a);
	return grid_color;
}

const Color Gridded_Light::eval (const Vector &p) const 
{
	//Return the trilinear result of P in grid
	Vec3f pos(p.X(), p.Y(), p.Z());
	
	//Create a sampler
	openvdb::tools::GridSampler<FloatGrid, openvdb::tools::BoxSampler> sampler(*grid);
	float density = sampler.wsSample(pos);
	Color color = S * exp(- density * K);
	return color;
}
