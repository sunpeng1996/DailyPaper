---
title: 'RSI-Prime: Training Models to Train Models'
title_zh: RSI-Prime：训练模型自主执行模型训练的数据集与训练方法
authors:
- Dewu Zheng
- Yang Ye
- Hongyu Zhang
- Jun Yu
- Yanlin Wang
affiliations:
- Sun Yat-sen University
- Mind Lab
- Chongqing University
- Harbin Institute of Technology, Shenzhen
arxiv_id: '2611.23138'
url: https://arxiv.org/abs/2611.23138
pdf_url: https://arxiv.org/pdf/2611.23138
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 递归自提升 · 模型训练能力优化
tags:
- Recursive Self-Improvement
- SFT
- LLM Agent
- Trajectory Annotation
- Loss Masking
one_liner: 构建含350条实验轨迹的RSI-Prime数据集，通过决策级掩码微调将LLM训练能力提升31.95%
practical_value: '- 做Agent轨迹微调时可复用决策级掩码方案：先对长流程轨迹做决策粒度的质量标注，仅监督关联全量高质量决策的消息，比步级掩码、工具失败掩码的效果提升更显著，适合电商推荐自动调优、广告投放策略迭代等长流程Agent的训练

  - 收集业务Agent的历史操作轨迹时，可参考其轨迹校验+过滤机制：增加预执行校验、独立进度监督、中断恢复能力保证轨迹完整性，再通过业务效果阈值（如相对业务指标提升>0.5）筛选有效轨迹，降低噪声数据的影响

  - 搭建业务场景的自动模型调优Agent时，可复用其决策分类框架：将流程拆分为数据准备、训练配置、评估诊断、模型交付、运维支持五大类决策，针对性优化各环节的决策质量，加速推荐/广告模型的自动迭代效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent已具备初步的模型训练规划、执行、迭代能力，但现有研究多聚焦工具链搭建，缺乏从历史训练经验中系统学习高质量决策的方案；直接全量微调实验轨迹会引入大量低质量行为噪声，制约Agent自主训练模型的效果，也阻碍递归自提升（RSI）系统的落地。
### 方法关键点
- 构建RSI-Prime数据集：覆盖数学推理、代码、指令微调等7类任务共350条完整模型训练轨迹，包含规划、训练、评估、迭代全流程，通过预执行校验、独立监督、中断恢复机制保证轨迹可靠性，仅保留目标模型相对提升超过基准50%的有效轨迹
- 细粒度决策标注：将实验流程拆分为分析、选择、执行三类节点，关联为完整决策，标注决策质量与所属动作类别（数据准备、模型训练、评估诊断等5大类20小类），通过多轮校验+人工审计保证标注准确率超97%
- 决策级损失掩码策略：仅对关联所有决策都通过质量校验的助手消息做SFT监督，其余消息做掩码，既保留完整实验上下文，又避免模型学习低质量决策
### 关键实验
基于GLM-5.3微调，在PostTrainBench基准测试：原模型整体得分36.56，全量轨迹微调得分45.61（相对提升24.75%），决策级掩码微调得分48.24（相对原模型提升31.95%），效果超过Opus 5.5、GPT-6.1等闭源Agent；对比步级掩码、工具失败掩码策略，决策级掩码在保留75%监督token的前提下取得最优效果，各环节决策质量通过率从87.25%提升至96.11%
### 核心结论
长流程Agent微调的核心不是学习完整轨迹，而是学习轨迹中的高质量决策，细粒度决策级监督的效果远优于简单过滤失败步骤的方案
