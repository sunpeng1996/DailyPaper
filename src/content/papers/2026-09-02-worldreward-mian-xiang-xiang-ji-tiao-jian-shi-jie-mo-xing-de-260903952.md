---
title: 'WorldReward: Reward Modeling for Camera-Conditioned World Models'
title_zh: WorldReward：面向相机条件世界模型的奖励建模
authors:
- Yibin Wang
- Zehan Wang
- Junshu Tang
- Zhimin Li
- Yujie Zhou
- Jiazi Bu
- Pengyang Ling
- Feng Han
- Zhixiong Zhang
- Long Xing
affiliations:
- Fudan University
- Tencent Hunyuan
- Shanghai Innovation Institute
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.03952'
url: https://arxiv.org/abs/2609.03952
pdf_url: https://arxiv.org/pdf/2609.03952
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 多模态世界模型 · 奖励建模
tags:
- Reward Modeling
- Vision-Language Model
- World Model
- Preference Learning
- Video Generation
one_liner: 基于VLM的成对偏好奖励模型，可统一评估相机条件世界模型的动作一致性与视觉质量
practical_value: '- 长序列偏好评估可借鉴「动作对齐分块+分块投票聚合」的思路，避免长上下文噪声导致局部信号丢失，可迁移到长会话用户行为偏好建模、长视频内容质量评估场景

  - 多模态偏好数据集构建可复用「大模型初标+工具Agent审核+定向人工复核」的流程，降低标注成本同时提升标注质量，可用于多模态内容推荐的偏好标签生成

  - 多维度统一奖励建模的思路可迁移到生成式内容推荐（如短视频、商品文案生成）的效果评估，同时对齐内容合规性、用户兴趣匹配度、生成质量等多维度要求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有相机条件世界模型的奖励评估存在维度割裂问题：几何类奖励仅能判断轨迹执行准确度，无法评估生成视频的视觉质量；图像类奖励仅能衡量单帧质量，无法捕捉动作一致性与时序连贯性，直接用VLM评估长视频又存在长上下文噪声大、局部动作证据易丢失的缺陷。
### 方法关键点
1. WorldReward为基于VLM的成对偏好奖励模型，将成对视频拆解为动作对齐的分块，结构化组织各分块视觉证据，分块评估后通过投票聚合得到视频级的动作一致性、视觉质量偏好得分
2. 构建大规模推理增强偏好数据集，采用前沿VLM生成结构化初判结果，经多轮工具Agent审核、定向人工复核优化标注质量
3. 开源人工标注的WorldReward-Bench，覆盖动作一致性、外观质量、运动质量三个评估维度
### 关键结果
在WorldReward-Bench上三个维度的人类偏好对齐度均超越GPT-5.5，分别高出3.42、1.45、3.56个百分点；用于HY-WorldPlay 1.5的RL后训练时，长短时长场景下的动作执行与视觉质量均有稳定提升
