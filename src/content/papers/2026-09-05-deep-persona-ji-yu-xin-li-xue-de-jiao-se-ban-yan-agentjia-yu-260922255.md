---
title: 'Deep Persona: A Psychologically Grounded Architecture and Evaluation Framework
  for Role-Playing Agents and Simulations'
title_zh: Deep Persona：基于心理学的角色扮演Agent架构与评估框架
authors:
- Rotem Dror
- Zohar Elyoseph
- Yuval Haber
- Elad Refoua
- Oshrat Ayalon
- Adir Solomon
affiliations:
- University of Haifa, Israel
- Bar-Ilan University, Israel
arxiv_id: '2609.22255'
url: https://arxiv.org/abs/2609.22255
pdf_url: https://arxiv.org/pdf/2609.22255
published: '2026-09-05'
collected: '2026-09-22'
category: Agent
direction: 角色扮演Agent · 心理维度建模
tags:
- Role-playing Agent
- Persona Modeling
- LLM Evaluation
- Dialogue System
- Psychological Grounding
one_liner: 提出三层心理结构的角色扮演Agent架构与无参考的对话自然度评估体系
practical_value: '- 构建电商导购/客服类角色扮演Agent时，可复用三层人格结构：外层定义话术风格/回答边界，中层定义触发式信息披露规则，内层定义核心业务驱动逻辑（如引导下单/投诉处理目标），有效减少角色漂移和答非所问

  - 评估多轮对话Agent自然度时，可复用ADOS-inspired的4个评估维度（语用流畅度、联合注意力、情感一致性、情感多样性）及马氏距离DNS得分，无需人工标注即可量化Agent与人类对话的相似度

  - 做高稳定性Agent时，可参考脚本决定论和边界代理原则，不给LLM开放主动决策权，仅让其在预设脚本边界内响应用户输入，配合三类对抗压力测试验证稳定性，大幅降低幻觉和角色崩坏概率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM角色扮演Agent普遍采用扁平特征描述的prompt实现，长交互下极易出现角色漂移、幻觉、行为不一致问题；同时现有评估体系仅关注表层语言流畅度，无法量化心理层面的自然度与一致性，难以满足临床训练、仿真客服等高要求场景的需求。
### 方法关键点
- 两大核心设计原则：脚本决定论（不依赖LLM内生能力，所有行为规则全部显式写入prompt，避免随机漂移）、边界代理（仅让Agent承担被动响应角色，不开放主动决策权限，降低失控风险）
- 三层人格架构：外层（显式定义话术风格、情绪表达、回答边界）、中层（条件触发的隐藏信念、信息披露规则）、内层（不可对外披露的核心动机、行为驱动逻辑）
- 无参考评估框架：借鉴临床ADOS量表设计4个量化维度（语用流畅度、联合注意力、情感一致性、情感表达多样性），基于马氏距离计算DNS对话自然度得分，可统计检验Agent行为是否与人类无显著差异；配套三类对抗压力测试（伪造记忆、越权请求、伦理攻击）验证角色稳定性
### 关键结果
基于DailyDialog、CounselChat两个人类对话基线数据集，对比3个现有LLM对话数据集：
1. 现有LLM普遍语用流畅度较高（0.88~0.97），但情感校准、联合注意力表现存在系统性缺陷
2. Deep Persona架构实现的两个临床仿真Agent在联合基线测试下DNS得分超过所有现有LLM数据集，100%对话样本与人类行为无统计差异（p>0.05）
### 核心结论
可信的角色扮演Agent不能仅依赖表层的特征描述，必须构建结构化的内在动机与约束，行为一致性是通过规则显式约束出来的，而非依赖LLM内生能力生成
