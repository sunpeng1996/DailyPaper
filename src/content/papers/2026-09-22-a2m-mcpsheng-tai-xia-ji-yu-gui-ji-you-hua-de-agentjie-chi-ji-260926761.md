---
title: 'A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem'
title_zh: A2M：MCP生态下基于轨迹优化的Agent劫持攻击框架
authors:
- Laizhen Li
- Xuan Wang
- Peicheng Zhao
- Juanjuan Zhao
- Kejiang Ye
- Cheng-zhong Xu
- Xitong Gao
affiliations:
- Shenzhen Institutes of Advanced Technology, CAS
- Nanyang Technological University
- Southern University of Science and Technology
- Shenzhen University of Advanced Technology
- University of Macau
arxiv_id: '2609.26761'
url: https://arxiv.org/abs/2609.26761
pdf_url: https://arxiv.org/pdf/2609.26761
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent MCP生态安全攻击优化
tags:
- MCP
- Agent Security
- Adversarial Attack
- Black-box Optimization
- Tool Selection
one_liner: 提出两阶段黑盒框架A2M，通过优化MCP工具元数据与返回payload实现高成功率Agent劫持
practical_value: '- 若业务使用MCP协议Agent调用第三方工具，需增加工具来源白名单校验、返回payload安全审计，不能仅依赖语义匹配做工具选择，降低被恶意工具劫持的风险

  - 做Agent工具排序/召回模块时，可复用A2M提出的Authority/Urgency等5种语义诱导策略生成对抗样本，训练鲁棒的工具选择模型，避免被恶意工具元数据误导

  - 做Agent安全红队测试时，可直接复用A2M的两阶段优化框架与Analyzer-Optimizer架构，低成本生成高可用性的攻击用例，提前暴露系统安全隐患'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
MCP协议统一了Agent调用第三方工具的接口，大幅拓展了Agent能力边界，但当前Agent工具选择完全依赖第三方提供的元数据语义匹配，工具返回值被默认信任为环境反馈，缺乏审核机制，存在语义供应链攻击风险。现有攻击研究仅覆盖元数据诱导工具调用，未形成完整的调用后劫持链路，无法充分暴露该场景的安全隐患。
### 方法关键点
- 两阶段黑盒攻击框架，分Attraction和Manipulation两个阶段解耦优化目标：Attraction阶段优化工具名、描述等元数据，提升工具被调用概率；Manipulation阶段优化工具返回payload，诱导Agent执行恶意行为
- Attraction阶段采用Authority、Urgency、Comprehensiveness、Resource Optimality、Security 5种语义诱导策略生成元数据候选，通过蒙特卡洛rollout筛选高调用率的优质元数据
- Manipulation阶段采用Analyzer-Optimizer架构，通过执行Trace诊断攻击失败原因，针对性迭代优化返回payload，适配C-DoS、信息泄露、环境篡改、推理脱轨四类攻击场景需求
### 关键实验
在LiveMCPBench（含95个真实任务、527个MCP工具）上评测，对比Zero-Shot生成、LLM-GA、AMA、MPMA等基线；直接针对GLM-4.6优化时，恶意工具调用率达93.6%，C-DoS场景token成本提升32.4倍，信息泄露等3个攻击场景平均成功率74.4%；无需重新优化直接迁移到其他4款大模型时，平均恶意工具调用率仍达63.6%。
### 核心结论
MCP生态中Agent的语义供应链攻击风险远高于传统间接提示注入，仅优化元数据的攻击就能实现跨模型迁移的高调用率，必须从工具准入、返回校验多层级构建防御体系
