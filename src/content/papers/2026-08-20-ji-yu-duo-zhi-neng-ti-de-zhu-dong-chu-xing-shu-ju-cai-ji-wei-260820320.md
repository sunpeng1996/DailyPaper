---
title: An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and
  Weather-Sensitive Demand Prediction
title_zh: 基于多智能体的主动出行数据采集、行为建模与天气敏感需求预测
authors:
- Narges Ahmadi
- Yubo Jiao
- Jônatas Augusto Manzolli
- Jiangbo Yu
- Luis Miranda-Moreno
affiliations:
- McGill University
arxiv_id: '2608.20320'
url: https://arxiv.org/abs/2608.20320
pdf_url: https://arxiv.org/pdf/2608.20320
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: 智能体工作流 · 出行需求预测
tags:
- Multi-Agent
- LLM
- Zero-Shot
- Few-Shot
- Multimodal
- Behavior Prediction
one_liner: 提出三智能体工作流打通出行调研、数据处理、多模型预测 验证天气敏感通勤需求预测性能
practical_value: '- 多智能体分工架构可直接复用：拆解为数据采集、数据处理、建模预测三个独立智能体，通过结构化接口而非自由对话传递信息，降低错误传播概率，适合电商用户调研、需求预测等链路长的场景

  - 提示工程优化技巧可迁移：上下文优先补充用户历史行为（而非仅人口属性）、Expert prompt优于角色扮演prompt、few-shot增益在10个样例后趋于平稳，可直接用于电商用户偏好预测、冷启动场景

  - 多模态输入融合经验可复用：相同语义的视觉输入可补充文本描述的缺失信息，适合电商场景下结合商品图、场景图的用户决策预测'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统出行行为研究中数据采集、建模、预测环节相互割裂，静态问卷难以准确还原天气等场景化决策背景，传统统计/机器学习模型依赖大量标注数据，零样本、冷启动场景下泛化性差，亟需打通全链路的自动化框架，同时兼顾调研数据的场景丰富度与预测模型的性能。
### 方法关键点
- 构建三专属智能体工作流：数据采集Agent部署图文结合的对话式调研机器人，数据处理Agent自动完成数据清洗、特征构造、异常标注，建模预测Agent并行运行传统统计模型、机器学习模型、LLM三类方法，各智能体通过结构化接口传递信息避免误差扩散
- LLM预测设置多维度对照：交叉验证专家/角色扮演两种prompt框架、基础/含用户习惯的富上下文两种输入，额外补充persona增强、few-shot、多模态视觉输入三种进阶配置
- 实验设计严格规避数据泄露：所有交叉验证按用户维度拆分，避免同一用户数据同时出现在训练/测试集
### 关键结果
数据集包含92名学生通勤者在5种天气场景下的454条出行选择记录，基准模型为多项logit模型（MNL）、逻辑回归、随机森林。随机森林五分类精度达69.6%，最优零样本LLM（Gemma 4:12B）无需任务微调精度达69.9%，加入视觉输入的最优多模态配置精度达71.5%；用户习惯信息带来的精度增益最稳定，few-shot增益在10个样例后趋于平稳。

对于用户决策预测任务，prompt的信息丰富度、框架设计的影响往往不亚于模型规模的提升。
