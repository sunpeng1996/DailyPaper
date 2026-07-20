---
title: 'Cura 1T: Specialized Model for Agentic Healthcare'
title_zh: Cura 1T：面向医疗智能体场景的专用大语言模型
authors:
- actAVA AI
- Haolin Chen
- Leon Qi
- Steve Brown
- Deon Metelski
- Tao Xia
- Joonyul Lee
- Qixuan Wang
- Kevin Riley
- Frank Wang
affiliations:
- actAVA AI
arxiv_id: '2607.15314'
url: https://arxiv.org/abs/2607.15314
pdf_url: https://arxiv.org/pdf/2607.15314
published: '2026-07-14'
collected: '2026-07-20'
category: Agent
direction: 医疗场景智能体专用LLM训练优化
tags:
- Domain-specific LLM
- Self-evolution Training
- Agentic LLM
- Healthcare AI
- Human-in-the-loop
one_liner: 通过人控自进化循环训练的医疗专用LLM，医疗任务表现顶尖且域外能力保持竞争力
practical_value: '- 垂直领域专用Agent训练可复用「人控自进化循环」框架：无需全量灌入领域数据，每轮针对失败case优化数据混合比例，避免单任务优化导致其他能力退化，适合电商导购、售后客服等垂直Agent模型迭代

  - 多能力兼顾的模型迭代思路可迁移到电商全链路Agent：无需针对用户咨询、商品推荐、工单处理分别训练独立模型，通过定向构造合成+人工审核的case集统一迭代，降低多任务模型的维护成本

  - 垂直领域模型评估可参考其「基准测试轨迹回溯」方法：从失败的全交互轨迹反推数据缺口，而非仅看最终准确率指标，大幅提升模型迭代效率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
医疗场景需同时覆盖患者咨询、多模态临床推理、交互式诊断、EHR工具调用等多类能力，现有专用LLM普遍存在单任务优化导致其他能力退化的问题，缺乏适配全链路医疗Agent需求的统一基座。
### 方法关键点
采用人门控自进化训练循环：每轮由训练Agent规划目标能力、完成模型训练、回溯基准测试的全轨迹、针对观测到的失败case动态调整数据混合策略，仅通过定向生成的合成样本+人工审核的优质样本迭代，无需全量更新通用医疗数据集，避免能力遗忘。
### 关键结果
在MedAgentBench、HealthBench等6项主流医疗基准测试中排名达顶尖水平，同时在域外推理、通用智能体基准测试中保持竞争力，无明显跨能力退化。
