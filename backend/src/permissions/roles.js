export const ROLE_PERMISSIONS = {
  "Super Admin": ["*"],

  "ERP Admin": [
    "users.read",
    "users.create",
    "users.update",
    "roles.read",
    "roles.manage",
    "products.read",
    "products.create",
    "products.update",
    "products.delete",
    "inventory.read",
    "inventory.adjust",
    "reports.read",
  ],

  "Inventory Manager": [
    "products.read",
    "products.create",
    "products.update",
    "inventory.read",
    "inventory.adjust",
    "reports.read",
  ],

  "Sales Manager": [
    "products.read",
    "customers.read",
    "sales.read",
    "sales.create",
    "sales.update",
  ],

  Staff: [
    "products.read",
    "inventory.read",
  ],

  Viewer: [
    "products.read",
    "inventory.read",
    "reports.read",
  ],
};

export function hasPermission(role, permission) {
  const permissions = ROLE_PERMISSIONS[role] ?? [];

  return (
    permissions.includes("*") ||
    permissions.includes(permission)
  );


