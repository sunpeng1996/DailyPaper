---
title: 'IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems'
title_zh: IQuest-Q1：面向CLI智能体的开源稀疏MoE基础模型
authors:
- A. Jian Yang
- An Huang
- Bo Dan
- Chen Mu
- Chengran Yang
- Chuan Shi
- Feng Chang
- Hongxin Li
- Hongyuan Tao
- Jinxing Zhang
affiliations:
- IQuest Research
arxiv_id: '2610.30949'
url: https://arxiv.org/abs/2610.30949
pdf_url: https://arxiv.org/pdf/2610.30949
published: '2026-10-21'
collected: '2026-10-23'
category: Agent
direction: Agent 专用大模型 · CLI交互能力优化
tags:
- MoE
- Agent
- CLI
- LLM
- RL
- SFT
one_liner: 开源总参320B激活15B的CLI优化Agent基础模型，多任务领先开源SOTA接近闭源水平
practical_value: '- 多阶段训练pipeline可直接复用：预训练→中期扩域→SFT→RL+多教师蒸馏→模型合并的流程，适合打造电商运营自动化、广告投放调优等垂直领域专用Agent，平衡通用能力和场景专项能力

  - MoE训练优化技巧可迁移：Stable SplitNorm、Muon优化器+μP参数化组合，能提升大模型训练稳定性与缩放效率，小模型搜索的学习率可零样本迁移到大模型，大幅降低大模型调参成本

  - Agent防奖励黑客方案可落地：环境预处理、执行时拦截、轨迹审计三层防护机制，可直接复用到推荐/广告Agent训练中，避免Agent钻规则漏洞（比如投放Agent恶意刷曝光、搜索Agent违规引流等问题）

  - MOPD多教师蒸馏方案适合业务部署：可将多个垂直领域专家模型的能力蒸馏合并到低激活参数的MoE模型中，在保留多场景能力的同时降低推理成本，适合端侧或高并发业务场景部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM-based Agent依赖CLI实现工具调用、代码执行、外部系统交互，是工业级Agent落地的核心交互路径，但现有开源模型普遍存在CLI交互能力弱、长Horizon任务稳定性差、跨脚手架适配性不足的问题，缺少专门面向CLI场景优化的开源基础模型，难以支撑Agent的大规模产业落地。
### 方法关键点
- 架构设计：采用稀疏MoE结构，总参数320B、单token激活参数仅15B，混合GQA与滑动窗口注意力，引入Stable SplitNorm提升模型深度利用率，结合Muon优化器+μP参数化实现跨模型尺度的超参零样本迁移，训练效率比同规模Qwen3-MoE高1.93倍
- 分阶段训练Pipeline：预训练阶段分两阶段逐步提升代码与STEM数据占比至70%；中期训练扩展数据域并逐步拉长上下文窗口至512K；SFT阶段用290B+Token训练基础CLI交互能力；后训练阶段结合多脚手架RL与MOPD多教师同策略蒸馏，融合4个不同领域专家模型的能力；最终通过跨阶段模型合并解决参数更新冲突，整合互补能力
- 训练防护机制：采用环境准备、执行时检查、轨迹审计三层防护，全链路过滤奖励黑客产生的无效训练数据，保障Agent能力对齐预期
### 关键结果
在8类Agent与编码基准上测试，对比DeepSeek-V4、GLM-5.3等开源SOTA模型：编码任务DeepSWE v1.1得分64.6、CyberGym得分84.5；通用Agent任务JobBench得分55.7、Agents' Last Exam得分29.6；内部CLI交互基准IQuest-CLIBench得分53.7，所有指标均为开源模型第一，部分能力接近Claude Opus 5、GPT-5.6 Sol等闭源SOTA。
> 最值得记住的话：面向垂直场景的Agent大模型，通过渐进式分阶段训练+多专家能力融合，可使用15B级激活参数达到接近千亿级闭源模型的领域性能，同时兼顾落地推理成本。
