---
title: 'MediSkill-Evo: Process-Constrained Self-Evolution for Evidence-Grounded Clinical
  Interaction'
title_zh: MediSkill-Evo：流程约束下证据驱动的临床交互Agent自进化系统
authors:
- Ruoyu Wu
- Shenfu Xie
- Yinqian Sun
- Haibo Tong
- Feifei Zhao
affiliations:
- 中科院自动化所类脑认知AI实验室
- 北京安全AI与超级对齐重点实验室
- 北京人工智能安全与治理研究院
- 中国科学院大学人工智能学院
- Long-term AI
arxiv_id: '2608.23397'
url: https://arxiv.org/abs/2608.23397
pdf_url: https://arxiv.org/pdf/2608.23397
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 自进化·安全流程约束
tags:
- Self-Evolving Agent
- Typed Memory
- Process Constraints
- Safety Alignment
- Clinical Agent
one_liner: 提出四类型记忆库与流程约束偏好框架，无需微调 backbone 实现临床Agent安全可控自进化
practical_value: '- 可复用类型化记忆库设计：将不同性质的知识（策略、规则、语义、操作）分库存储，独立做验证、更新和权限管控，适合电商Agent/推荐系统里把业务规则、召回策略、用户画像等知识解耦，避免互相污染

  - 流程约束偏好harness可直接迁移到业务Agent：先做硬规则校验过滤非法候选，再做多维度打分排序选最优动作，适合电商客服Agent、营销决策Agent的动作生成，降低违规风险

  - 自进化记忆的版本冻结机制：训练阶段更新记忆，测试阶段用不可变快照，可解决推荐/Agent系统在线迭代时的行为一致性问题，避免进化过程中出现不可控的输出'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有临床交互Agent仅靠最终诊断标签无法验证决策过程是否符合医疗流程和证据边界，自进化记忆通常把不同类型的知识混在同一个检索接口，缺乏分类管控和安全校验，容易出现证据误用、流程违规等安全问题，亟需一种不需要微调大模型、同时能保障决策可溯源、符合流程约束的自进化方案。

### 方法关键点
- 四类型分库记忆架构：分别存储临床技能、流程规则、符号语义、测量操作四类知识，每类知识独立完成来源校验、安全检查、重放验证后才发布为不可变的测试快照，避免不同性质的知识互相干扰
- 流程约束偏好Harness：先基于规则触发强制流程动作，否则生成多候选，先经符号校验过滤使用无效/不可得证据的候选，再通过安全优先的临床流程critic多维度打分选最优动作，所有决策全程可审计
- 全程不微调backbone大模型，所有能力迭代都通过外部记忆更新实现，迭代成本低、行为可管控

### 关键结果
数据集采用MIMIC-IV衍生的300例全流程交互测试集、180例受控压力测试集、100例NEJM多模态测试集，对比AgentClinic、ExPeL、MemP等7个基线：Qwen3.6-Flash backbone下，诊断准确率从61.33%提升到69.00%，参考治疗意图覆盖率从33.62%提升到66.44%，严重错误率从31.00%降到16.33%；受控压力测试下，患者行为目标恢复率93.61%，时序证据恢复率100%，分诊红色预警恢复率92.22%，均远超基线。

**最值得记住的一句话**：当记忆的类型不仅决定检索内容，还决定其验证规则和决策权限时，自进化Agent的行为才能变得可控可信。
