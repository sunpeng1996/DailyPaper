---
title: 'Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic
  Visual Reasoning'
title_zh: Reframe：面向智能体视觉推理的观测对齐多教师同策略蒸馏
authors:
- Haozhi Yuan
- Handong Li
- Yifan Zhang
- Qianshan Wei
affiliations:
- Nanjing University
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2611.12886'
url: https://arxiv.org/abs/2611.12886
pdf_url: https://arxiv.org/pdf/2611.12886
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: Agent 多教师蒸馏视觉推理优化
tags:
- Multi-Teacher Distillation
- On-Policy Distillation
- Visual Agent
- Tool Use
- Reinforcement Learning
one_liner: 提出观测对齐两阶段多教师同策略蒸馏框架，解决视觉Agent工具结果忽视问题，统一图像视频推理能力
practical_value: '- 训练调用工具的Agent时，可引入「原始输入随机dropout+工具返回观测依赖奖励」，强制模型真正使用工具结果，避免工具调用后仍依赖原始输入的幻觉问题，适合电商商品图文识别、视频卖点提取类Agent

  - 多教师同策略蒸馏（MOPD）合并跨域能力时，可在轨迹rollout阶段插入观测门控，修复无效/低质量工具调用后再蒸馏，减少错误观测对后续蒸馏的干扰，适合整合多场景专用专家能力到统一Agent

  - 训练数据构造时可参考论文的5步清洗流程，过滤不需要工具就能回答、证据不足的样本，提升工具调用相关训练的数据质量，降低标注噪声'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前视觉Agent存在**观测忽视**问题：调用工具后仍不使用返回结果，仅依赖原始输入推理；且传统多教师同策略蒸馏（MOPD）仅优化监督信号，不干预rollout轨迹，错误工具动作导致的无效观测会大幅降低蒸馏效果；同时混合SFT+RL范式训练统一的图像视频多模态Agent，效果会弱于单模态专用模型，需要更有效的同策略训练范式。

### 方法关键点
- 两阶段训练框架Reframe，无需任务特定SFT冷启动
  1. **GD-GRPO**训练单模态专家：设计包含回答正确性、工具调用行为、观测匹配度的复合奖励，首次成功调用工具后随机以0.5概率丢弃原始视觉输入，强制模型依赖工具返回结果；按dropout标记分组计算优势，消除难度差异干扰
  2. **OG-MOPD**蒸馏统一模型：rollout时检查学生工具调用的IoU，低于阈值则替换为标注的正确工具动作，修复观测后再继续蒸馏；学生生成的token用标准MOPD监督，注入的正确工具动作token用NLL单独监督
- 构造包含63K图像QA、37K视频QA的Reframe-100K数据集，经过5步清洗保证标注质量，同时支持RL和蒸馏阶段训练

### 关键结果
在14个图像、视频Benchmark上测试，对比Mix-RL、原生MOPD及现有视觉Agent，效果如下：
- 图像平均准确率69.48%，超过原生MOPD 1.29个点，超过现有最优SOTA 11.71个点；视频平均准确率53.10%，超过原生MOPD 0.78个点，超过现有最优SOTA 8.86个点
- 观测依赖度达到75.53%，是对比模型的1.8~3.9倍；工具带来的增益达到+5.23，是对比模型的3.6~5.4倍

### 最值得记住的一句话
有效工具调用的核心是两个要素——获得的观测是必要的、且是有效的，两者缺一不可
