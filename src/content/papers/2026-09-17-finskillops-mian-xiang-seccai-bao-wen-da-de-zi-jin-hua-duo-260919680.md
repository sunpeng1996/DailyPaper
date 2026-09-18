---
title: 'FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA'
title_zh: FINSKILLOPS：面向SEC财报问答的自进化多智能体系统
authors:
- Yanzhang Ma
- Zhenghan Tai
- Hanwei Wu
- Sizhe Guan
- Jianliang Lei
- Hailin He
- Chaolong Jiang
- Jijun Chi
- Tung Sum Thomas Kwok
- Bohuai Xiao
affiliations:
- SimpleWay.AI
- McGill University
- University of Toronto
- University of California, Los Angeles
- The Chinese University of Hong Kong
arxiv_id: '2609.19680'
url: https://arxiv.org/abs/2609.19680
pdf_url: https://arxiv.org/pdf/2609.19680
published: '2026-09-17'
collected: '2026-09-18'
category: MultiAgent
direction: 多智能体自进化 · 技能生命周期管理
tags:
- MultiAgent
- SelfEvolving
- SkillManagement
- RAG
- FinancialQA
- LifecycleGovernance
one_liner: 提出带严格技能生命周期管控的自进化多智能体架构，实现金融问答无回归性能迭代
practical_value: '- 可复用技能治理框架：将业务badcase归类为带触发条件的技能补丁，上线前依次通过目标错误集验证、历史正确样本回归校验、负例误触发校验三道门，完全适配电商搜索/推荐的badcase迭代场景，避免修复旧问题引入新回退。

  - 多角色智能体分工可直接迁移：根据业务域拆分专用智能体（如电商场景拆分为用户理解、商品匹配、合规校验、文案生成角色），仅激活相关角色参与推理，兼顾领域准确性和推理效率。

  - 零训练迭代链路可复用：badcase根因诊断后生成自然语言修复指令，仅在query分解、答案合成两个节点通过prompt注入生效，无需重新训练模型，大幅降低业务迭代成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有垂直领域QA系统部署后性能固定，SEC财报问答中反复出现的周期不匹配、实体混淆、证据误用、计算错误无法自动修复；通用自进化Agent无严格迭代管控，修复错误时容易引入新的回归问题，无法满足高可靠性要求。

### 方法关键点
- 架构分在线服务、离线进化两条链路：在线侧将财报解析为带模态、周期、实体标签的检索块，编排器按需激活通用、量化、市场、法律、公司5类专用分析师智能体，做多路径检索后合成答案，技能指令在query分解、答案合成两个节点注入。
- 离线badcase闭环：先对错误做根因分类，高频错误自动生成带适用条件、触发规则、执行逻辑的自然语言技能，新技能上线必须满足三个条件：目标错误集准确率提升、历史正确样本无回归、负例无误触发。
- 全生命周期技能管理：支持技能版本迭代、替换、退役，始终保持技能库精简，避免指令冲突。

### 关键结果
- 在3个公开、3个内部金融QA benchmark上，冻结技能库的FINSKILLOPS加权准确率、参考一致性均为最优，内部增强数据集上加权准确率从初始3.70提升至4.55。
- 12轮落地测试中，33个候选技能仅6个通过校验上线，监控集非正确率从20.0%降至12.5%，无历史正确样本回归。

### 最值得记住的一句话
自进化系统的核心不是迭代速度，而是可控的迭代边界，每一次更新都要在收益、回退风险、误触发率之间做严格平衡。
