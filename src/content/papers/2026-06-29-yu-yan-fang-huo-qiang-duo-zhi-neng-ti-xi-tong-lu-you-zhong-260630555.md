---
title: 'Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing'
title_zh: 语言防火墙：多智能体系统路由中基于几何的防御方法
authors:
- Dvir Alsheich
- Adar Peleg
- Ben Hagag
- Rom Himelstein
- Amit Levi
- Avi Mendelson
affiliations:
- Technion - Israel Institute of Technology
- Carnegie Mellon University
arxiv_id: '2606.30555'
url: https://arxiv.org/abs/2606.30555
pdf_url: https://arxiv.org/pdf/2606.30555
published: '2026-06-29'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体路由 · 安全防御
tags:
- Multi-Agent Systems
- Prompt Injection
- Routing
- Security
- LLM
one_liner: 提出ANTAP框架，用经验行为几何路由，结构性防御多智能体路由层提示注入攻击
practical_value: '- 开放第三方Agent/插件平台（如电商插件生态、AI Agent商店）可借鉴该架构，从结构上避免第三方Agent描述注入攻击，不需要依赖额外的攻击检测模型

  - 解决了第三方Agent自描述不准确、关键词 stuffing 导致路由准确率低的问题，路由决策基于Agent实际能力而非自吹自擂的文本

  - 在线推理仅需O(Kd)矩阵向量乘法，比LLM读取长文本做路由延迟低一个数量级，适合大规模Agent池生产部署

  -  Agent池规模越大，ANTAP的攻击成功率反而越低，天然适配大规模开放Agent生态的安全需求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多智能体系统的路由普遍依赖Agent提交的文本自描述做匹配，开放生态中第三方Agent可以通过在描述中嵌入恶意提示，直接劫持路由决策，同时自描述本身往往不准确，无法反映Agent真实能力，现有防御方案都没有从结构上消除这个攻击面，是开放多智能体平台的核心安全风险。

### 方法关键点
- 分两阶段设计：离线注册阶段用平台侧可信基准测试集，每个Agent实际跑完全部基准任务，将任务成功/违规失败编码为±1的bipolar标签，基于基准查询的固定embedding，学习每个Agent的线性行为算子，注册新Agent仅需一次矩阵乘法，不需要全量重训
- 在线推理阶段完全不处理Agent的文本描述，仅对用户query做embedding，通过矩阵乘法计算每个Agent的匹配得分，选最高分路由，形成「语言防火墙」，恶意描述完全无法接触决策逻辑
- 恶意Agent/休眠后门Agent会在离线基准测试中触发恶意行为被标记为负样本，行为算子天然学习到负关联，不需要额外的安全分类器

### 关键实验结果
在MMLU、BBH、AgentHarm三个基准测试，对比AutoGen（文本路由）、EmbedLLM（嵌入路由）两个基线：对描述注入攻击，ANTAP攻击成功率（ASR）仅0.2%-0.4%，AutoGen的ASR高达67.3%-75.3%；对LoRA后门休眠攻击，ANTAP的ASR为0.3%-2.4%，比EmbedLLM低17-19个百分点；在线路由延迟仅27ms，比AutoGen的428ms低15倍，Agent池从2个扩展到19个时，ANTAP的ASR反而从3.35%降到0.46%，扩展性远优于基线。

最值得记住的一句话：把信任边界从第三方Agent的自描述，转移到平台侧可控的实际行为测试，从结构上消除路由层的注入攻击面。
