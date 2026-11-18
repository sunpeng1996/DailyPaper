---
title: 'MillBill: A Machining Agent with Geometric Feedback'
title_zh: MillBill：具备几何反馈能力的机械加工智能体
authors:
- Gennadii Savrasov
- Artem Slavin
- Soslan Kabisov
- Andrey Kuznetsov
- Anton Konushin
- Dmitrii Zhemchuzhnikov
affiliations:
- Lomonosov Moscow State University
- Innopolis University
- FusionBrain Lab
arxiv_id: '2611.22565'
url: https://arxiv.org/abs/2611.22565
pdf_url: https://arxiv.org/pdf/2611.22565
published: '2026-11-16'
collected: '2026-11-18'
category: Agent
direction: 机械加工领域Agent决策执行解耦优化
tags:
- LLM Agent
- Geometric Feedback
- Execution Verification
- Tool Path Planning
- Open LLM
one_liner: 提出决策与几何执行验证解耦的机械加工Agent MillBill，加工效果优于主流前沿模型方案
practical_value: '- 可复用Agent决策-执行解耦架构：将LLM擅长的领域知识决策，与不擅长的高精度数值计算/仿真执行拆分，适合电商供应链规划、广告投放效果仿真等需要专业计算的垂直Agent场景

  - 可迁移闭环反馈迭代范式：执行模块返回仿真验证结果给LLM迭代优化决策，可直接用于电商素材生成、商品选品等需要落地效果校验的业务场景

  - 中尺寸开源LLM落地思路：采用本地部署的中等规模开源模型做垂直领域决策引擎，相比调用闭源前沿模型成本更低、数据安全性更高，适合企业内部Agent落地'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM生成机械加工流程时需同时处理工艺决策与高精度几何数值计算，出错率高且无落地验证能力，传统计算机辅助工艺规划仍高度依赖人工。

### 方法关键点
1. 架构解耦：拆分工艺决策与几何执行验证流程，本地部署的开源LLM仅负责输出加工操作、切削参数等工艺方案，独立几何模块生成刀具路径、仿真材料去除并返回反馈用于方案迭代
2. 装夹规划优化：不仅考虑加工面可见性，额外纳入现有刀具的物理可达性约束

### 关键结果
基于Qwen3.8-27B实现的MillBill，在仿真加工任务中指定公差内的目标表面积占比指标，显著优于自行构建几何与刀具路径工作流的前沿大模型方案。
