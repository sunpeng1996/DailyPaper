---
title: 'HyperClaim: Fine-Grained Cross-Modal Hypergraph Reasoning for Video Misinformation
  Detection'
title_zh: HyperClaim：面向视频虚假信息检测的细粒度跨模态超图推理
authors:
- Xiangbo Wang
- Jiasheng Zhang
- Xingtong Yu
- Luoqiang Lei
- Delvin Ce Zhang
affiliations:
- 杭州电子科技大学通信工程学院
- 西安电子科技大学计算机科学与技术学院
- 新加坡管理大学计算与信息系统学院
- 谢菲尔德大学计算机学院
arxiv_id: '2607.28375'
url: https://arxiv.org/abs/2607.28375
pdf_url: https://arxiv.org/pdf/2607.28375
published: '2026-07-30'
collected: '2026-08-01'
category: Multimodal
direction: 跨模态内容理解 · 超图推理
tags:
- Cross-Modal
- Hypergraph Reasoning
- Misinformation Detection
- Multimodal Fusion
- Fine-grained Feature
one_liner: 提出跨模态稀疏异质超图框架，无需外部工具实现SOTA视频虚假信息检测
practical_value: '- 做短视频带货虚假宣传识别、广告合规校验等跨模态内容审核场景时，可复用稀疏异质超图建模文本token、视频帧、ASR文本的高阶交互，替代传统全局融合减少细粒度信息损失

  - 跨模态特征对齐环节可借鉴confidence-aware过滤+源预算机制，压缩无效特征单元，降低推理算力开销，适配实时/端侧部署需求

  - 残差文本-视频校准+差异感知读出的组合trick，可迁移至多模态召回排序场景，提升不同模态特征的融合效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频虚假信息检测的全局多模态融合、自由式推理范式，易丢失查询短语、上下文文本、短视频帧片段间的局部细粒度交互信息；成对图结构无法有效捕获多路径跨模态高阶依赖。
### 方法关键点
1. 以标题/配套文本为类声明查询，在查询token、证据token、采样帧之上构建稀疏异质超图；
2. 引入置信度感知过滤、源预算机制，生成紧凑的文本-帧、短时序证据单元，压缩无效特征；
3. 采用自适应软关联推理+残差文本-视频校准方案，通过差异感知读出层聚合文本、视觉、超边三类状态。
### 关键结果
在FactGuard时序评测协议下，FakeSV、FakeTT、FakeVV三个数据集上准确率分别达83.7%、82.0%、87.3%，性能超过主流判别式、推理类基线方案。
