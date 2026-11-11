---
title: 'Micius-Flash: Lightweight Agentic Intelligence for Engineering'
title_zh: Micius-Flash：面向工程领域的27B参数轻量级智能体模型
authors:
- Hongcheng Gao
- Weiheng Li
- Yipeng Wei
- Yu Lei
- Shuo Sun
- Yi Li
- Yajiao Wang
- Jie Luo
- Jianwei Wen
- Xinyi Zhou
affiliations:
- Micius Team
arxiv_id: '2611.10015'
url: https://arxiv.org/abs/2611.10015
pdf_url: https://arxiv.org/pdf/2611.10015
published: '2026-11-03'
collected: '2026-11-11'
category: Agent
direction: 工程领域智能体 · 多教师同策略蒸馏
tags:
- Agent
- LLM
- Multimodal
- Knowledge Distillation
- Domain Adaptation
one_liner: 采用知识树数据飞轮+多教师同策略蒸馏，打造27B多模态工程智能体，性能优于同规模基线
practical_value: '- 知识树驱动的数据飞轮可迁移到垂类推荐/Agent的数据构建流程：比如电商场景搭建商品/用户运营知识树，定向合成训练样本，再用模型bad
  case反哺知识树扩容，大幅提升垂域训练数据的覆盖度与质量

  - 多教师同策略蒸馏（MOPD）方案可复用：把召回、排序、多模态理解、工具调用等多个垂直专家模型的能力合并到一个统一推理模型，降低线上部署成本，同时避免多能力干扰问题

  - Micius Harness的架构可参考：在电商客服、运营Agent等场景搭建统一的工具权限管控、业务产物校验、执行环境隔离模块，保障线上调用的安全性与结果可靠性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用大模型在工程等垂直领域存在三大痛点：一是垂域知识碎片化、训练数据覆盖不足；二是多类任务能力整合易出现相互干扰、通用能力退化；三是缺乏对接专业工具与真实业务流的执行基建，难以落地。
### 方法关键点
- 数据层：设计知识树驱动的数据飞轮，分为知识树构建与扩容、定向数据合成、质量校验+难例增强三个阶段，通过模型bad case反哺数据迭代，闭环提升垂域数据覆盖度与质量
- 训练层：先微调4个垂直专家模型（知识推理/硬件编码/多模态理解/Agent工具调用），再通过多教师同策略蒸馏（MOPD）将多专家能力整合到统一27B学生模型，避免能力冲突
- 工程层：推出Micius Harness工作平台，封装能力权限管控、工程产物可视化、统一远程执行三大模块，打通模型到专业工具/真实业务流的落地路径
### 关键结果
在20+基准共1.5万条样本上测试，硬件编码基准平均得分64.2%，较同规模通用基线高15.0个百分点；半导体专属Agent基准得分62.4%，较同规模通用基线高17.2个百分点；通用推理能力保持与同规模大模型相当的水平，PCB设计、芯片流程自动化等落地案例验证了其工具调用、多步规划与迭代优化能力。
> 垂域Agent的落地不能只靠单点模型微调，需要数据构建、能力整合、工程基建全链路的系统性优化才能实现可用的业务效果
