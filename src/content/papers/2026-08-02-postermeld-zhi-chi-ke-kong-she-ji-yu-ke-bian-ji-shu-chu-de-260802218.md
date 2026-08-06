---
title: 'PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design
  Diversity with Editable Print-Ready Outputs'
title_zh: PosterMELD：支持可控设计与可编辑输出的多智能体论文转海报生成系统
authors:
- Haojie Hu
- Chenhao Dang
- Yaojia Liu
- Hengrui Kang
- Conghui He
- Weijia Li
affiliations:
- Tsinghua Shenzhen International Graduate School, Tsinghua University
- Tongji University
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- Renmin University of China
arxiv_id: '2608.02218'
url: https://arxiv.org/abs/2608.02218
pdf_url: https://arxiv.org/pdf/2608.02218
published: '2026-08-02'
collected: '2026-08-06'
category: MultiAgent
direction: 多智能体协作 · 生成式内容生产
tags:
- MultiAgent
- VLM
- Generative Content
- Pipeline Optimization
- Cost Efficiency
one_liner: 提出模板条件多智能体论文转海报pipeline，实现高打印可用率、低成本的可编辑海报生成
practical_value: '- 多智能体任务编排可参考「模板插槽预填充+确定性门控+VLM校验+有限修复」架构，降低生成失败率，可复用在电商详情页、广告物料生成场景

  - 复杂生成任务可先做容量感知的插槽内容规划再渲染，避免排版/内容溢出问题，适合海报、商品介绍页自动生成流程

  - 用冻结VLM做生成内容多维度（工艺/和谐度/表达性）自动打分，无需人工标注即可快速迭代 pipeline，可用于广告物料效果评估

  - 业务向生成系统优先输出可编辑格式（如PPTX）而非图片，降低用户二次修改成本，可直接迁移到电商营销物料、活动海报生成'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有论文转海报系统存在三类缺陷：仅评估完成态输出掩盖请求级失败、直接生成图片无法编辑元素、编码Agent工作流成本过高，无法满足实际场景对可编辑性、打印可用性的要求。
### 方法关键点
1. 采用模板条件多智能体 pipeline：先基于容量感知的插槽引导内容撰写，再执行渲染，规避内容溢出问题
2. 引入确定性门控+VLM审核机制，将失败请求路由到有限修复流程，降低整体失败率
3. 支持显式设计控制，同一份论文可生成多版本海报，输出可编辑PPTX和PNG两种格式
### 关键结果数字
在621篇论文测试集上，打印可用率（PRR）达81.3%，是P2P的3.4倍、PosterGen的5.2倍；单请求平均成本仅0.38美元，为Codex+Skill方案的3.5%；同时在多输出生成方法中取得最高的CHE（工艺-和谐度-表达性）评分，原生可编辑性和设计可控性完全保留。
