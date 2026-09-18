---
title: 'SenseFuse: Label-Free Fusion of Image and Shape Encoders for Open-Vocabulary
  3D Instance Segmentation'
title_zh: SenseFuse：面向开放词汇3D实例分割的图像形状编码器无标注融合方法
authors:
- Euiseok Han
- Tri Ton
- Hwanhee Kim
- Seungyeon Ryu
- Chang D. Yoo
arxiv_id: '2609.20475'
url: https://arxiv.org/abs/2609.20475
pdf_url: https://arxiv.org/pdf/2609.20475
published: '2026-09-17'
collected: '2026-09-18'
category: Other
direction: 开放词汇3D实例分割 · 跨模态无标注融合
tags:
- 3D Instance Segmentation
- Open-Vocabulary
- Multimodal Fusion
- Label-free
- Scene Understanding
one_liner: 提出无标注跨模态融合框架SenseFuse，仅优化掩码标注阶段提升开放词汇3D实例分割性能
practical_value: '- 多模态特征融合可优先选择错误模式无重叠的异源特征组合，避免同源特征重复误差，可复用在商品多模态召回/排序场景

  - 无标注场景下可通过单样本无标注敏感度指标自适应计算融合权重，无需额外标注成本，适合冷启动场景的多模态模型迭代

  - 仅优化下游打分/分配阶段的轻量改造方案，可复用在现有推荐/搜索管线的快速迭代，无需重构全链路'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有开放词汇3D实例分割方案仅依赖2D图像特征或其蒸馏表示，未利用3D形状信息，且2D编码器存在遮挡误判等固有缺陷，同源编码器易出现重复错误。
### 方法关键点
1. 验证2D图像与3D形状编码器错误模式高度不重叠，天然具备互补性
2. 提出SenseFuse无标注融合框架，仅改造现有管线的掩码标注阶段，侵入性极低
3. 设计自适应权重选择机制，基于单场景无标注提案毫秒级计算场景级融合权重，最大化无标注敏感度指标
### 关键结果
在ScanNet200、Replica、ScanNet++所有测试设置下均提升标注精度，覆盖oracle权重可实现收益的67%~100%（中位数93%），22个测试设置中21个的实例AP获得提升。
