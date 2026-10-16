---
title: 'Beyond Policy Rollouts: Embedding-Space Directional Exploration with Anchored
  Noise for LLM RLVR'
title_zh: 基于锚定噪声的嵌入空间定向探索提升LLM RLVR训练效果
authors:
- Daijiao Liu
- Huiyi Wang
- Lina Yao
- Dong Gong
affiliations:
- University of New South Wales (UNSW Sydney)
arxiv_id: '2610.16105'
url: https://arxiv.org/abs/2610.16105
pdf_url: https://arxiv.org/pdf/2610.16105
published: '2026-10-11'
collected: '2026-10-16'
category: Training
direction: LLM RLVR训练 · 探索优化
tags:
- RLVR
- GRPO
- Exploration
- LLM Training
- Reinforcement Learning
one_liner: 不增加rollout预算，通过嵌入层锚定噪声拓展RLVR探索空间，提升推理LLM训练效果
practical_value: '- 电商/导购Agent做RLHF/RLVR微调时，可直接复用EDEN的锚定噪声方案，在不增加rollout采样成本前提下解决样本同质化问题，提升解空间覆盖度

  - 扰动样本的「绝对优势筛选+降权更新」trick可迁移到所有生成式任务的RL训练流程，既引入探索信号又避免训练不稳定

  - 嵌入层单次追加扰动的设计无需修改模型结构、解码逻辑与线上推理链路，业务侧可零侵入接入现有RL训练pipeline

  - 探索强度cosine升温调度的思路可复用，适配业务场景数据分布复杂、训练稳定性要求高的特性，避免初期噪声过大导致训练崩溃'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR是当前推理类LLM post-training的主流方案，受限于rollout生成成本，通常每prompt仅采样8-16条轨迹，同策略采样的轨迹高度同质化会导致组相对优势信号消失，政策熵快速崩塌，解覆盖度不足。现有优化方案（调高采样温度、熵奖励、非对称裁剪等）均从修改采样分布或训练目标切入，未从rollout生成源头上解决同质化问题，单纯增加rollout数量成本高且效果提升有限。

### 方法关键点
- 不增加总rollout预算，替换每组内小比例标准rollout为嵌入层锚定噪声扰动的生成结果，训练结束后推理逻辑完全无变更
- 预训练前构造固定锚点嵌入库，每个prompt组共享一个采样锚点，叠加独立高斯噪声生成扰动嵌入，追加到prompt末尾后喂入模型，单次扰动即可影响整个生成过程
- 按批维度对扰动生成的轨迹按绝对优势排序，保留top p比例高信息量样本，将其优势降权后与标准样本共同加入GRPO更新，平衡探索性与训练稳定性
- 扰动样本的采样温度采用cosine升温策略，初期低温度保证训练稳定，后期高温度增强探索强度

### 关键结果
在Qwen2.5 0.5B/1.5B/7B三个模型尺度、8个数学推理基准上对比GRPO、高温采样、Clip Higher等baseline：1.5B模型平均Pass@1提升2.44点、Pass@8提升3.06点；7B模型平均Pass@8提升3.64点，AIME竞赛数据集Pass@256最高提升13.33点；仅用16条rollout的EDEN效果超过32条rollout的GRPO，训练过程中零优势样本组占比降低8.6%。

> 最值得记住：从rollout生成源端做定向嵌入扰动，比单纯修改输出采样或训练目标的探索效率更高，且完全不影响线上推理
