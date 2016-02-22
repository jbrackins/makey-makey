/*************************************************************************//**
 * @file <SKELETON>.cpp
 *
 * @brief SOURCE - <SKELETON> Main Source file. 
 *
 * @mainpage <SKELETON>
 *
 * @section course_section <COURSE_SECTION>
 *
 * @author <AUTHOR_NAME>
 *
 * @date <CURRENT_DATE>
 *
 * @par Professor:
 *         <PROFESSOR_NAME>
 *
 * @par Course:
 *         <COURSE_NAME>
 *
 * @par Location:
 *         <COURSE_LOCATION>
 *
 * @section program_section Program Information
 *
 * @details
 * <PROGRAM_DETAILS>
 *
 * @section compile_section Compiling and Usage
 *
 * @par Compiling Instructions:
 *      (Linux) - make
 *
 * @par Usage:
 @verbatim

 @endverbatim
 *
 * @section todo_bugs_modification_section Todo, Bugs, and Modifications
 *
 * @par Modifications and Development Timeline:
 @verbatim
 Date              Modification
 ----------------  --------------------------------------------------------------
 <CURRENT_DATE> * Project Initialization.

 @endverbatim
 *
 ******************************************************************************/

 #include "../inc/<SKELETON>.h"

/******************************************************************************
 *
 * NAMESPACES
 *
 ******************************************************************************/

using namespace std;

/******************************************************************************
 *
 * GLOBALS
 *
 ******************************************************************************/

 /**************************************************************************//**
 * @author <AUTHOR_NAME>
 *
 * @par Description:
 * Main Function
 *
 * @param[in] argc - the number of arguments from the command prompt.
 * @param[in] argv - a 2d array of characters containing the arguments.
 *
 * @returns 0 - Program Ends Gracefully.
 *
 *****************************************************************************/
int main(int argc, char ** argv)
{
  usage( argv );
  
  return 0;
}

/**************************************************************************//**
 * @author <AUTHOR_NAME>
 *
 * @par Description:
 * Print program Usage statements
 *
 * @returns nothing
 *
 *****************************************************************************/
void usage( char ** argv )
{
  cout << "Usage: " << argv[0] << " ";
  
  //ADD PARAMETERS
  cout << "arg1 arg2 arg3 etc.";
  cout << "\n\n";
  cout << "arg1 - arg1 description" << endl;
  cout << "arg2 - arg2 description" << endl;
  cout << "arg3 - arg3 description" << endl;
  cout << "etc. - ..." << endl;
}