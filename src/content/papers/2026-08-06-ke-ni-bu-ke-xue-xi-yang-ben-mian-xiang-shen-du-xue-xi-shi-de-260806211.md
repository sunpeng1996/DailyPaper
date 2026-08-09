---
title: 'Reversible Unlearnable Examples: Towards the Copyright Protection in Deep
  Learning Era'
title_zh: 可逆不可学习样本：面向深度学习时代的版权保护
authors:
- Binze Wang
- Jinyu Tian
- Xingrun Wang
- Xiaochen Yuan
- Jianqing Li
arxiv_id: '2608.06211'
url: https://arxiv.org/abs/2608.06211
pdf_url: https://arxiv.org/pdf/2608.06211
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 深度学习数据版权保护
tags:
- Copyright Protection
- Unlearnable Examples
- Watermarking
- Data Perturbation
- Deep Learning Security
one_liner: 提出兼顾防非法训练与泄露溯源的可逆不可学习样本版权保护方案
practical_value: '- 可复用不可学习扰动生成思路，给电商自有商品图、营销素材添加扰动，防止被第三方爬取后用于训练生成式AI、图像识别类竞品模型

  - 双水印提取策略可迁移到业务自有版权内容的溯源场景，解决内容加扰动后水印提取准确率下降的问题

  - 针对UGC/PGC素材池的版权保护，可参考该方案同时实现防非法训练、泄露溯源的双重能力'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
深度学习训练高度依赖大规模数据集，现有不可学习样本方案仅防御非法训练，未覆盖数据泄露后的所有权溯源需求，直接叠加水印与不可学习扰动存在负向干扰，无法同时应对两类版权风险。
### 方法关键点
1. 生成最小化模型输入输出互信息的扰动，诱导训练模型学习输入图像的无关特征，实现泛化性较强的防非法训练能力；
2. 设计双水印提取器策略，消除不可学习扰动对水印提取的副作用，支持数据泄露后的所有权溯源。
### 关键结果
在ImageNet、CIFAR10、Pets三类图像数据集上验证可实现全链路图像版权保护，相关代码已开源。
