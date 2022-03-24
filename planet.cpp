#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
using namespace std;
#define GPIO "/sys/class/gpio/"
#define FLASH_DELAY 50000

class PLANET{ 
    private:
	string planetName;
	int planetRadius;
	int planetDistance;
	int planetDensity;
	int planetMass;
	void writeSysfs(string path, string filename, string value);

    public:
	PLANET(int planetRadius);
	virtual void getRadius;
	virtual void getDistance;
	virtual void getDensity;
	virtual void getMass;	
};

PLANET :: PLANET(int->planetRadius){
	this->planetRadius=planetRadius;
	planetName = string(GPIO "gpio") + to_string(planetRadius) + string("/");
	writeSysfs(string(GPIO), "export", to_string(planetRadius));
	usleep(100000);
	writeSysfs(planetName, "direction", "out");
}

void PLANET::writeSysfs(string path, string filename, string value){
	ofstream fs;
	fs.open((path+filename).c_str());
	fs << value;
	fs.close();
}

void PLANET::getRadius(){
	writeSysfs(planetName, "value", "1");
}
void PLANET::getDistance(){
	writeSysfs(planetName, "value", "0");
}
void PLANET::getDensity(){



	ifstream fs;
	fs.open((planetName + "value").c_str());
	string line;
	cout << "HELLLO";
	while(getline(fs,line)) cout << line << endl;
	fs.close();
}

PLANET::PLANET(){
	cout <<"temp message" << planetRadius << endl;
	writeSysfs(string(GPIO), "unexport", to_string(planetRadius);
}

int main(int argc, char* argv[]){
	cout << "Starting akjahdfhj" << endl;
	PLANET
