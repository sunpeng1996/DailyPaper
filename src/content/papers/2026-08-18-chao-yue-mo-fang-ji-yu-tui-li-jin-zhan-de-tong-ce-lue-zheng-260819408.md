---
title: 'Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress'
title_zh: 超越模仿：基于推理进展的同策略蒸馏奖励过滤方法
authors:
- Chen Yang
- Haiyuan Wan
- Rengrong Xiong
- Yize Chen
- Danny H. K. Tsang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
- Zhejiang University
- University of Alberta
arxiv_id: '2608.19408'
url: https://arxiv.org/abs/2608.19408
pdf_url: https://arxiv.org/pdf/2608.19408
published: '2026-08-18'
collected: '2026-08-25'
category: Training
direction: 大模型同策略蒸馏 · 推理监督优化
tags:
- On-Policy Distillation
- Process Reward
- Reward Filtering
- LLM Reasoning
- Knowledge Distillation
one_liner: 提出R2-OPD框架，通过检测推理进展与蒸馏奖励的排序冲突过滤不可靠监督，提升推理模型蒸馏效果
practical_value: '- 做LLM微调/蒸馏的业务场景（比如Agent多轮导购推理、query理解小模型蒸馏、商品文案生成模型压缩）可复用冲突检测思路：无需直接将PRM作为优化目标，仅用PRM作为监督信号质量判断器，过滤老师模型给出的不合理惩罚，避免压制学生的有效推理路径，降低蒸馏副作用

  - 处理噪声大的对齐信号（比如用户行为反馈、LLM自动标注的排序信号）时可复用符号一致段合并trick：将相邻同方向的信号合并为粗粒度单元，抵消中间估计误差，降低噪声对排序判断的干扰，尤其适合多步骤用户路径、推理路径的信用分配

  - 小模型蒸馏落地时，30%左右的低质量监督信号过滤比例在多个推理任务上效果最优，可作为蒸馏信号过滤的默认超参数基线调整'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-Policy Distillation (OPD) 默认老师模型的token级相似度奖励等价于推理质量，但实际中常出现学生偏离老师路径、但实际能提升推理正确率的步骤反而被惩罚的情况，压制了有效推理路径；而直接结合Process Reward (PR) 又存在信号尺度不一、噪声大的问题，两者难以直接融合。

### 方法关键点
- 提出R2-OPD框架，不将PR作为额外优化目标，而是作为独立的推理进展参考，仅用于检测蒸馏信号的可靠性
- 先按话语标记切分推理段，合并相邻符号一致的PR段，通过累减抵消中间段的估计误差，得到更稳定的粗粒度推理单元
- 对每个合并段计算平均KL散度，比较PR排序与KL散度排序的局部冲突，冲突越高说明蒸馏信号越不可靠，按冲突得分排序过滤最高的30%段的蒸馏监督
- 过滤后仅保留与推理进展一致的监督信号更新学生模型，避免压制有效推理

### 关键实验
在DAPO-Math-17K数据集上训练，采用DeepSeek-R1-Distill-Qwen-1.5B、Qwen3-1.7B两个学生模型，对比标准OPD及5种最新OPD变体，在AIME 2024、AIME 2025、OlympiadBench三个推理基准上，R2-OPD平均比标准OPD的avg@4提升2.51个点，pass@4提升4.46个点，比最优基线Uni-OPD的avg@4提升4.28个点，pass@4提升5.17个点。

> 最值得记住的一句话：蒸馏小模型时不用盲目模仿老师的每一步输出，用过程奖励做监督信号的质量校验，过滤掉和实际效果冲突的监督，比全量模仿效果更好。
