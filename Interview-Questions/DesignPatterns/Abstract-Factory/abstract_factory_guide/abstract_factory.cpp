#include <iostream>
#include <memory>
using namespace std;

class Button {
public:
    virtual void render() = 0;
    virtual ~Button() {}
};
class Checkbox {
public:
    virtual void check() = 0;
    virtual ~Checkbox() {}
};
class WindowsButton : public Button {
public:
    void render() override { cout << "Rendering Windows Button\n"; }
};
class WindowsCheckbox : public Checkbox {
public:
    void check() override { cout << "Windows Checkbox checked\n"; }
};
class LinuxButton : public Button {
public:
    void render() override { cout << "Rendering Linux Button\n"; }
};
class LinuxCheckbox : public Checkbox {
public:
    void check() override { cout << "Linux Checkbox checked\n"; }
};
class GUIFactory {
public:
    virtual unique_ptr<Button> createButton() = 0;
    virtual unique_ptr<Checkbox> createCheckbox() = 0;
    virtual ~GUIFactory() {}
};
class WindowsFactory : public GUIFactory {
public:
    unique_ptr<Button> createButton() override {
        return unique_ptr<Button>(new WindowsButton());
    }
    unique_ptr<Checkbox> createCheckbox() override {
        return unique_ptr<Checkbox>(new WindowsCheckbox());
    }
};
class LinuxFactory : public GUIFactory {
public:
    unique_ptr<Button> createButton() override {
        return unique_ptr<Button>(new LinuxButton());
    }
    unique_ptr<Checkbox> createCheckbox() override {
        return unique_ptr<Checkbox>(new LinuxCheckbox());
    }
};
void buildUI(GUIFactory& factory) {
    auto button = factory.createButton();
    auto checkbox = factory.createCheckbox();
    button->render();
    checkbox->check();
}
int main() {
    WindowsFactory windows;
    LinuxFactory linux;
    cout << "Windows UI:\n";
    buildUI(windows);
    cout << "\nLinux UI:\n";
    buildUI(linux);
}
