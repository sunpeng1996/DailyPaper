---
title: 'Learning More by Training Less: Uncertainty-Guided Progressive Contraction
  for Efficient Reasoning Post-Training'
title_zh: 不确定性引导渐进收缩的LLM推理高效后训练方法
authors:
- Suorong Yang
- Jiaxin Wang
- Jiaming Su
- Chentao Yue
- Furao Shen
- Peng Ye
- Soujanya Poria
affiliations:
- National University of Singapore
- Nanjing University
- Fudan University
- The University of Sydney
- The Chinese University of Hong Kong
arxiv_id: '2610.12933'
url: https://arxiv.org/abs/2610.12933
pdf_url: https://arxiv.org/pdf/2610.12933
published: '2026-10-08'
collected: '2026-10-13'
category: Training
direction: LLM推理训练 · 高效蒸馏
tags:
- Efficient Training
- Knowledge Distillation
- Uncertainty Quantification
- Chain-of-Thought
- SFT
one_liner: 两阶段渐进收缩筛选高价值推理轨迹，仅用0.22%全量SFT预算保持并提升LLM推理性能
practical_value: '- 业务场景做垂域LLM（如电商导购Agent、搜索query推理模型）SFT时，可直接复用两阶段数据筛选逻辑，仅用不到1%的训练样本就能达到全量训练效果，大幅降低训练成本

  - 小模型蒸馏（如端侧LLM、轻量化推理模型）可复用弱到强迁移结论，不需要大参数老师模型，用小参数模型标注的不确定性数据就能提升大模型性能，降低大模型API调用成本

  - 对接商用黑盒LLM做知识蒸馏时，不需要访问模型logits、梯度等内部信息，仅通过多轮采样续跑即可计算过程不确定性，可直接对接GPT、DeepSeek等API生产高价值训练数据

  - 搜索推荐的多轮语义理解、复杂query推理任务训练时，可借鉴过程不确定性思路筛选难例，优先训练推理分支多、容易出错的样本，提升模型在边缘case上的表现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM推理能力后训练依赖不断扩大的CoT语料规模，训练成本线性飙升但性能增益边际递减，现有数据筛选方法仅依赖最终答案的正确性、终端置信度，忽略推理过程中的分支不确定性，无法实现极致的训练效率提升。
### 方法关键点
- 教师侧不确定性收缩：对每条教师生成的CoT轨迹，在中间推理状态做Monte Carlo多轮续跑采样，计算每个状态的分支结果不确定性，聚合得到整条轨迹的过程不确定性得分，仅保留Top ρ的高不确定性正确轨迹组成候选池，候选池可跨不同学生模型复用
- 学生感知优化收缩：SFT阶段先对候选池做一轮探测前向，计算每条轨迹的长度归一化响应loss，仅选择loss最高的M条轨迹做后续参数更新，训练过程中动态重算loss调整训练集，适配学生的实时学习状态
### 关键实验
在数学推理、科学推理等10+benchmark测试，覆盖Qwen、Gemma、Llama、Mistral等多个模型族，对比全量SFT、普通CoT蒸馏等baseline：仅用0.22%的全量SFT优化预算，训练速度最高提升800×，推理性能平均提升3.6%~4%；支持弱到强迁移，1.7B小老师可提升14B学生性能最高14.4%；训练得到的9B学生性能超过30B~671B量级的开源/闭源大推理模型。
### 核心结论
推理后训练的核心不是盲目扩大数据规模，而是精准识别高学习价值的轨迹，仅用千分之几的样本即可超越全量训练效果
