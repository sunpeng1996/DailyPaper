---
title: Region-Level Black-Box Defense Against Stealthy Embedding-Space Backdoors in
  CLIP
title_zh: 面向CLIP嵌入空间隐式后门的区域级黑盒防御方法
authors:
- Ahmed Abdelnaby
- Mohamed Elmahallawy
affiliations:
- Washington State University
arxiv_id: '2609.31558'
url: https://arxiv.org/abs/2609.31558
pdf_url: https://arxiv.org/pdf/2609.31558
published: '2026-09-25'
collected: '2026-09-28'
category: Multimodal
direction: 多模态模型 · 后门安全防御
tags:
- CLIP
- Backdoor Defense
- Black-box Defense
- Embedding Attack
- Semantic Inpainting
one_liner: 提出轻量全黑盒防御方案CLIPGuard，通过分块扰动检测+语义修复对抗CLIP嵌入空间隐式后门攻击
practical_value: '- 电商图文检索、商品分类、内容审核等场景下以CLIP为多模态底座时，可直接接入CLIPGuard实现黑盒后门防御，无需修改模型参数或获取原始训练数据

  - 「分块检测嵌入扰动+仅修复可疑区域」的思路可迁移至多模态输入去噪场景，在保留有效内容的同时过滤恶意水印、隐式触发符号等干扰

  - 无参数、全黑盒的防御架构可快速适配已上线的CLIP相关服务，无需重新训练模型即可完成安全能力迭代'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
CLIP作为主流多模态底座被广泛应用于图文检索、分类等场景，但存在嵌入空间后门攻击风险：仅需毒化极少量图文对即可植入隐式触发，直接篡改嵌入空间表达，极难检测。现有防御方案大多依赖模型参数、梯度或干净验证集，黑盒部署场景下难以落地，且现有黑盒方法对小尺寸、分布外触发的定位精度差。
### 方法关键点
提出CLIPGuard全黑盒轻量防御方案，通过计算图像分块的嵌入扰动识别恶意区域，仅对可疑片段做语义修复，最大程度保留正常视觉内容与图文对齐质量。
### 关键结果
在STL-10、ImageNet数据集及BadCLIP、BadNets、混合补丁等多类攻击场景下，攻击成功率最低降至1.05%，同时干净样本准确率保持最高86.34%，性能显著优于CleanCLIP、CleanerCLIP等现有黑盒防御方案。
