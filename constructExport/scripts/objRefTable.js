const C3 = self.C3;
self.C3_GetObjectRefTable = function () {
	return [
		C3.Plugins.Sprite,
		C3.Behaviors.Sin,
		C3.Plugins.Touch,
		C3.Plugins.Mouse,
		C3.Plugins.Mouse.Cnds.OnObjectClicked,
		C3.Plugins.Touch.Cnds.OnTouchObject,
		C3.Behaviors.Sin.Cnds.IsEnabled,
		C3.Behaviors.Sin.Acts.SetEnabled,
		C3.Plugins.System.Cnds.Else
	];
};
self.C3_JsPropNameTable = [
	{Sine: 0},
	{Sprite: 0},
	{button: 0},
	{Touch: 0},
	{Mouse: 0}
];

self.InstanceType = {
	Sprite: class extends self.ISpriteInstance {},
	button: class extends self.ISpriteInstance {},
	Touch: class extends self.IInstance {},
	Mouse: class extends self.IInstance {}
}