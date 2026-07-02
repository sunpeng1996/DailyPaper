---
title: Hierarchical Experimentalist Agents
title_zh: 分层实验者智能体HExA：基于主动实验的上下文内技能学习框架
authors:
- Abhranil Chandra
- Sankaran Vaidyanathan
- Utsav Dhanuka
- Varun Gandhi
- Scott Niekum
affiliations:
- University of Massachusetts Amherst
arxiv_id: '2606.29315'
url: https://arxiv.org/abs/2606.29315
pdf_url: https://arxiv.org/pdf/2606.29315
published: '2026-06-27'
collected: '2026-07-02'
category: Agent
direction: Agent 主动实验与可迁移技能学习
tags:
- LLM Agent
- in-context learning
- skill bank
- active exploration
- zero-shot transfer
one_liner: 提出训练无关的HExA分层智能体框架，通过主动实验构建可迁移技能库提升未知域任务表现
practical_value: '- 新品冷启动、新流量场运营等电商新场景的Agent可直接复用HExA的actor-evolver-retriever无训练架构，通过业务交互数据自动沉淀结构化运营/投放策略库，大幅降低冷启动试错成本

  - 跨域推荐场景可复用分层技能蒸馏逻辑：将不同业务域沉淀的运营规则、人群定向策略等，蒸馏为「适用条件+策略内容+避坑指南」的结构化格式，零样本迁移到新业务域，无需重新标注训练数据

  - 策略检索模块可复用奖励加权排序逻辑：给沉淀的策略打业务效果分（如GMV提升率、点击率增量），每次任务前检索Top N高价值策略注入Agent上下文，兼顾效果与上下文长度控制'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent依赖预训练参数知识或固定RAG增强，在完全未知的新域（如新业务场景、无先验规则的环境）下表现极差，且每次任务都从零开始试错，无法沉淀可复用的经验，探索成本极高。
### 方法关键点
- 无训练三层架构：兼容任意黑盒LLM，由actor（工具调用LLM，与环境主动交互生成实验轨迹）、evolver（同LLM，基于轨迹的成功/效率奖励标签，蒸馏结构化技能库，包含「适用条件+策略原理+错误规避」三类内容，每条技能带奖励分）、retriever（按奖励分召回Top M高价值技能、Top N错误记录，注入下一轮actor上下文）组成
- 分层技能进化：不仅从成功轨迹提取策略，还从失败轨迹中提取中间有效步骤和错误规避方案，技能库随新实验持续迭代优化，而非固定不变
- 零样本跨域迁移：evolver可移除源域技能的场景绑定参数，重新适配到目标域，无需目标域任何交互数据
### 关键结果
- 基于PHYRE构建INTERPHYRE物理推理基准，对比ReAct、Reflexion、GRPO微调等基线
- 最难Catapult任务上，Claude Sonnet 4.6基线仅2%成功率，HExA最高提升至77%，单任务迭代次数减少37%
- 零样本跨域迁移场景下，仅用简单域沉淀的技能库，Catapult任务直接达到44%成功率，超基线42个百分点
- 低数据量场景下，HExA样本效率是GRPO微调的1.5~3.2倍，小模型上也有明显收益
### 核心结论
交互数据稀缺的新场景下，上下文内沉淀结构化可复用技能的效率，远高于从零试错或直接微调模型。
