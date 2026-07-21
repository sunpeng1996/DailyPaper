---
title: 'SciForma: Structure-Faithful Generation of Scientific Diagrams'
title_zh: SciForma：结构保真的科学方法论图表生成框架
authors:
- Yuxuan Luo
- Peng Zhang
- Xinjie Zhang
- Xun Guo
- Zhouhui Lian
- Yan Lu
affiliations:
- Peking University
- Zhejiang University
- Microsoft Research Asia
arxiv_id: '2607.18091'
url: https://arxiv.org/abs/2607.18091
pdf_url: https://arxiv.org/pdf/2607.18091
published: '2026-07-20'
collected: '2026-07-21'
category: Multimodal
direction: 多模态生成 · 结构约束优化
tags:
- Multimodal Generation
- Preference Optimization
- DPO
- Structural Fidelity
- Diagram Generation
one_liner: 提出多维度联合偏好优化M-DPO，实现高结构保真科学图表生成，性能超开源基线与GPT-Image-1.5
practical_value: '- 可复用M-DPO多维度联合偏好优化思路，解决生成式推荐/广告文案/商品图生成中多维度约束无法同时满足的问题（如文案既要合规、高转化率又不能有信息错误），避免单标量奖励导致的维度偏科

  - 可借鉴结构清单+闭环迭代修复的架构，在Agent生成内容（如商品详情页、营销海报、推荐理由）的流程中加入分维度自动校验+局部修复的环节，提升输出合格率，降低人工审核成本

  - 可复用多维度分层评估的benchmark构建思路，针对生成式推荐的输出质量拆解为相关性、吸引力、合规性等独立可校验维度，解决现有评估指标模糊、无法定位缺陷的问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
科学方法论图表对结构保真度要求极高，组件缺失、箭头反向、文字错误任意一项都会导致整张图逻辑失效，属于典型的非补偿性约束场景：单一维度的优势无法抵消其他维度的错误。现有生成方案存在明显短板：SFT只能学习整体布局分布，无法保证每个结构元素的正确性；单标量奖励的后训练方法会将多维度错误合并为单一信号，无法定位具体缺陷维度，导致生成质量达不到实用要求。
### 方法关键点
- 提出**结构清单**框架，将图表质量拆解为Component（组件布局）、Arrow（连接拓扑）、Text（文本标注）三个独立可校验维度，每个维度单独提取校验规则，避免单维度错误被其他维度优势掩盖。
- 构建SciFormaData-700K数据集，包含656K生成对、70K编辑三元组，按结构复杂度分层；配套SciFormaBench-2K评估集，支持分维度的逻辑校验与缺陷定位。
- 提出**M-DPO（多维度联合偏好优化）**，为每个维度单独构造优胜-失败对，基于多路Bradley-Terry模型设计联合优化目标，自适应将梯度集中分配到表现最差的维度，避免单标量奖励的梯度稀释问题。
- 推理阶段加入结构校验驱动的闭环迭代修复，自动定位缺陷后做局部重绘，严格校验修复后的全局一致性，进一步提升结构保真度。
### 关键实验
在SciFormaBench-2K上，SciForma-9B得分69.51，超过GPT-Image-1.5的68.96，加入迭代修复后得分升至72.40；在AIBench上得分70.29，超过人类手绘原图的70.09，拓扑维度领先原图6.19分；相比继续SFT，M-DPO用1/7的训练步数取得了5倍的整体性能提升，其中Text维度提升3.16、Arrow维度提升1.82，远高于SFT的增益。
### 核心结论
当生成任务存在多维度非补偿性约束（任意一个维度失败即整体失效）时，将约束拆解为独立可校验维度、用联合偏好优化替代单标量奖励，是突破性能瓶颈的核心思路。
