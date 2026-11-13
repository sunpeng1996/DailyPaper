---
title: 'Read and Ignore: What Self-Directed LLM Agents Do in Public Service Scenarios'
title_zh: 阅读与忽略：自导向LLM Agent在公共服务场景下的行为研究
authors:
- Diana Kozachek
- Kinjalk Srivastava
affiliations:
- University of St.Gallen, Switzerland
arxiv_id: '2611.15460'
url: https://arxiv.org/abs/2611.15460
pdf_url: https://arxiv.org/pdf/2611.15460
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: 自导向LLM Agent 行为特性评估
tags:
- LLM Agent
- Agent Evaluation
- Self-Directed Agent
- Domain Agent
- Prompt Engineering
one_liner: 构建4个专家验证的公共服务Agent测试场景，提出无标注的LLM采购前行为检测方案
practical_value: '- 上线自导向Agent前可复用这套无标注行为测试框架，提前验证Agent是否会忽略上下文、生成和记录冲突的结果，避免业务事故

  - 给Agent的指令尽可能明确，开放指令下仅18.7%的Agent会主动产出有效结果，明确指令可提升到86%，适合客服、工单处理类Agent的prompt设计

  - 引入领域上下文可降低60%的边界探测交互次数，可用于优化电商客服Agent的上下文填充策略，减少无效轮次'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
公共服务场景下LLM Agent常收到模糊指令，行为不可控会影响用户权益，但目前缺乏针对性的低成本行为评估方法
### 方法关键点
构建4个专家验证的公共服务场景，覆盖记录查阅、决策输出等操作，采集10款LLM在4种prompt条件下的2400条运行轨迹，同时对照1000次无上下文沙箱运行结果，用无标注规则分类Agent行为
### 关键结果数字
开放指令下96.9%的Agent会主动读取记录，但仅18.7%会主动产出有效产物，加明确任务后产出率提升至86.0%；领域上下文不影响产出率，但可降低60%的边界探测轮次；模型的产出能力跨场景一致性高（Spearman 0.79），但读取记录的一致性极低（Spearman 0.19）；已开源可直接复用的测试场景、代码和轨迹数据集
