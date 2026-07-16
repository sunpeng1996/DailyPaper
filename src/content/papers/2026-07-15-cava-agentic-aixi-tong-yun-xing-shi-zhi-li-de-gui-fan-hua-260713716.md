---
title: 'CAVA: Canonical Action Verification and Attestation for Runtime Governance
  of Agentic AI Systems'
title_zh: CAVA：Agentic AI系统运行时治理的规范化动作验证框架
authors:
- Zexun Wang
affiliations:
- Ond Holdings Inc.
arxiv_id: '2607.13716'
url: https://arxiv.org/abs/2607.13716
pdf_url: https://arxiv.org/pdf/2607.13716
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent运行时治理 · 动作语义归一化
tags:
- Agent Governance
- Action Canonicalization
- Runtime Security
- Policy Enforcement
- Attestation
one_liner: 提出异构运行时Agent动作归一化层，解决跨环境动作治理语义不一致、审批易绕过问题
practical_value: '- 对电商自动化运营、营销投放、客诉处理等业务Agent，可复用CAVA的动作归一化思路，避免基于原始文本/首token的规则被别名、嵌套命令绕过，提升运行时安全

  - 可参考语义模式层设计，将批量改价、大额优惠券发放、用户数据导出等业务风险抽象为通用可路由的语义模式，避免零散编写业务规则，降低维护成本

  - 指纹绑定+可验证收据的设计可复用在Agent审批流程中，解决「审批内容与实际执行动作不一致」的问题，满足电商合规审计要求

  - 开放核心+托管层的架构拆分可参考：核心归一化、哈希校验逻辑开源保证可验证性，业务定制规则、parser作为托管层变现，平衡开放性和商业价值'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent运行时异构性极强，同一业务动作可能以shell命令、SDK调用、浏览器事件、托管Agent trace等完全不同的形式存在，导致现有治理方案失效：基于原始文本的规则易被等价语法重写绕过，基于首token的规则易被env、sudo、bash -c等包装器隐藏真实动作，审批绑定到展示文本而非实际执行语义，跨运行时审计无法复用规则，也无法复现审批与执行的关联关系。
### 方法关键点
- 定义规范化运行时动作对象，包含schema版本、运行时类型、工具ID、归一化操作、风险类别、影响系统、可逆性、目标上下文等核心字段，屏蔽不同运行时的表达差异
- 设计6阶段治理协议：捕获原始事件→归一化为标准动作对象→识别可路由通用语义模式→基于规范字段生成唯一确定性哈希指纹→将审批、策略结果绑定到指纹而非原始文本→关闭动作并附加执行证据，可选签名、上链等增强证明
- 新增语义模式层，将动作+边界上下文+数据上下文映射为通用风险模式（如外部数据导出、权限提升、治理规则篡改等），避免零散定制业务规则
### 关键结果
基于96个种子场景扩展为384个跨4类运行时的变体数据集，对比原始文本规则、首token规则两个工业界常用baseline，CAVA在语义等价召回、语义分离精度、包装器绕过捕获率、假阳性控制、审批绑定正确率等9项核心指标全部达到100%，两个baseline绝大多数指标为0。
### 最值得记住的结论
没有稳定的动作语义层，审批只会绑定到字符串，trace只会绑定到运行时特有记录，跨执行环境的证据可复现性无从谈起。
