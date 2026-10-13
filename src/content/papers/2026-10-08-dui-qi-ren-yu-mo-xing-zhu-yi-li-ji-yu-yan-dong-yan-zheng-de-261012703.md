---
title: 'Bridging Human and Model Attention: Explainability Analysis of CNN, Mamba,
  and ViT Architectures with Gaze-Based Validation'
title_zh: 对齐人与模型注意力：基于眼动验证的CNN、Mamba与ViT架构可解释性分析
authors:
- Marco Stefani
- Edoardo Parpaiola
- Matteo Bino
- Gianluca Caregnato
- Francesco Roncolato
- Daniel Fusaro
- Loris Nanni
- Alberto Pretto
affiliations:
- Department of Information Engineering (DEI), University of Padova, Padova, Italy
arxiv_id: '2610.12703'
url: https://arxiv.org/abs/2610.12703
pdf_url: https://arxiv.org/pdf/2610.12703
published: '2026-10-08'
collected: '2026-10-13'
category: Other
direction: XAI 视觉架构注意力与人类感知对齐
tags:
- XAI
- CNN
- Vision Transformer
- Vision Mamba
- Saliency Map
- Eye Tracking
one_liner: 用人类眼动数据量化对比CNN、ViT、Mamba三类视觉架构注意力与人类感知的对齐度
practical_value: '- 多模态推荐视觉模块选型参考：通用商品理解场景优先选CNN，其全局注意力更贴合普通用户视觉感知习惯；需识别商品细粒度特征（如材质、logo）时选ViT；医疗/合规类垂类场景可选用Mamba，可解释性更优

  - 可复用这套可解释性量化框架：将模型注意力归因图与用户眼动热图经标准化归一化转空间概率分布，用JS、卡方、皮尔逊三个互补指标量化模型与用户注意力的对齐度，适用于商品图优化、推荐结果可解释性验证等场景

  - 商品主图/广告创意优化可参考不同架构注意力特性：对接CNN类识别模型的场景可突出全局视觉印象，对接ViT类模型的场景可强化关键细节特征的呈现'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
高风险深度学习场景受合规要求约束需明确模型决策机制，现有XAI研究多为定性分析，缺乏不同主流视觉架构注意力与人类感知对齐度的系统量化评估。
### 方法关键点
1. 以人类眼动数据为真值，设计标准化归一化pipeline，将模型事后归因图与人眼注视热图统一映射为空间概率分布；
2. 覆盖细粒度分类、医疗影像、情感识别3类场景，针对CNN、ViT、ViM分别采用适配的XAI方法生成注意力显著性图；
3. 选用JS相似度、卡方相似度、皮尔逊相关3个互补指标，分别度量支撑重叠、质量差异、结构协变三类对齐特性。
### 关键结果
- 通用场景下CNN的全局扩散显著性图与人类感知相关性最高；
- ViT注意力聚焦补丁级细粒度微特征，适合判别类任务；
- Mamba在医疗任务可解释性表现优异，但自然图像场景下强度分布与人类感知偏差大，支撑重叠接近1的同时线性相关性趋近于0
