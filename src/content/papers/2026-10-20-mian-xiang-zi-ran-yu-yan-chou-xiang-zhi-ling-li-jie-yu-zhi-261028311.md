---
title: 'From Abstraction to Action: DSLs for Natural Language Abstraction Interpretation
  and Execution'
title_zh: 面向自然语言抽象指令理解与执行的领域特定语言方法
authors:
- Amit Lisha
- Reut Tsarfaty
affiliations:
- Bar-Ilan University, Israel
arxiv_id: '2610.28311'
url: https://arxiv.org/abs/2610.28311
pdf_url: https://arxiv.org/pdf/2610.28311
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent 指令执行 · 领域特定语言
tags:
- Domain-Specific-Language
- Instruction-Following
- Agent
- Program-Synthesis
- Abstraction
one_liner: 验证人工 curated DSL 可大幅提升 LLM 执行抽象指令效果，指出 LLM 自主诱导 DSL 仍不稳定
practical_value: '- 电商导购/客服Agent可针对高频业务操作（如改地址、退差价、批量优惠券发放）人工封装DSL原语，大幅降低LLM处理抽象用户需求（如“帮我把这个订单所有商品都申请保价”）的错误率

  - 生成式推荐/智能搜索场景中，可将常用召回、排序、规则过滤逻辑封装为DSL，让LLM基于用户自然语言需求（如“推100-200元销量TOP10的户外露营灯”）直接生成调用DSL的执行链路，相比端到端生成结果准确率更高

  - 业务落地优先使用人类专家梳理的DSL，当前LLM自主诱导的DSL稳定性差，暂不建议直接上线，仅可作为DSL迭代的辅助参考'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM作为Agent执行自然语言指令时，性能随指令抽象程度提升显著下降：用户输入通常是压缩的抽象表述，需拆解为大量具体操作，现有直接生成结果、通用代码生成的方案均无法很好适配领域特有抽象概念，执行准确率低。
### 方法关键点
- 引入DSL作为自然语言抽象到具体动作的中间层，封装领域高频可复用操作，LLM仅需生成调用DSL的代码即可完成执行
- 人工构建HEXAGONS任务专用DSL HEXAGEN，遵循三大设计原则：覆盖领域核心抽象原语、接口命名与文档自解释、鲁棒输入校验与错误提示
- 提出LLM自主诱导DSL的三阶段流程：抽象发现（识别指令中重复计算模式）、方法实现（基于基础库生成可执行代码）、文档生成（输出LLM可读取的API说明）
### 关键结果
- HEXAGONS基准测试中，人工DSL辅助代码生成比直接预测F1最高提升10个绝对点，达到人类F1水平（0.853）；抽象程度越高收益越大，Level 3抽象指令下F1最高比直接预测高0.21
- TEXT2CAD真实场景中，DSL方案比直接生成代码的VLM偏好率最高提升22.9%，同时降低执行失败率
- LLM自主诱导的DSL峰值性能接近人工DSL，但稳定性极差，整体性能比人工DSL低3~10个F1点
### 核心结论
人工定义的领域抽象中间层是当前提升LLM Agent执行准确率最有效的手段之一，LLM自主生成可靠领域抽象层仍是待解决的开放问题
