union(){
translate([15,15,0])rotate([0,0,45])cube([44, 1, 1], center=true);
translate([0,0,0])rotate([0,0,45])cube([1, 88, 1], center=true);
translate([25.7,25.7,0])rotate([0,0,0]) cylinder(r=8, h=1, center=true);
translate([-25.7,25.7,0])rotate([0,0,0]) cylinder(r=8, h=1, center=true);
translate([25.7,-25.7,0])rotate([0,0,0]) cylinder(r=8, h=1, center=true);
*translate([-25.7,-25.7,0])rotate([0,0,0]) cylinder(r=8, h=1, center=true);
}//3dot marker



union(){
    translate([0,0,0])cube([66, 1, 1], center=true);

    translate([0,33,0])cube([66, 1, 1], center=true);
    translate([0,-33,0])cube([66, 1, 1], center=true);
    translate([0,0,0])cube([1, 66, 1], center=true);

    translate([33,0,0])cube([1, 66, 1], center=true);
    translate([-33,0,0])cube([1, 66, 1], center=true);
} //grid marker


