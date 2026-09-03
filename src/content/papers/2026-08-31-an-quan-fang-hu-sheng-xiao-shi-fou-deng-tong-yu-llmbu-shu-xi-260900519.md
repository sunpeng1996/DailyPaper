---
title: The Safeguard Worked. Is the LLM System Safer?
title_zh: 安全防护生效是否等同于LLM部署系统更安全？
authors:
- Pingyu Wu
- Weiming Zhang
- Nenghai Yu
affiliations:
- University of Science and Technology of China
- Hefei AiDA Lab
arxiv_id: '2609.00519'
url: https://arxiv.org/abs/2609.00519
pdf_url: https://arxiv.org/pdf/2609.00519
published: '2026-08-31'
collected: '2026-09-03'
category: Eval
direction: LLM安全 · 部署场景防护效果评估
tags:
- LLM Safety
- Security Evaluation
- Deployment Guardrail
- Adversarial Attack
- Risk Assessment
one_liner: 提出统一部署视角的LLM安全评估标准，指出局部安全防护得分高不代表全局部署系统更安全
practical_value: '- 线上LLM驱动的导购/推荐Agent做安全评估时，不能只看本地安全拦截率，要补充全链路渗透测试，验证绕过防护后的风险残留

  - 迭代安全防护策略时，不要仅优化局部拦截指标，需结合业务场景做全局风险校验，避免投入大量资源优化指标后仍存在可被利用的漏洞

  - 对Agent调用工具的权限管控、行为审计等周边安全能力的建设，优先级不低于prompt层面的安全拦截规则优化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM安全防护评估仅依赖拒绝率、攻击成功率、政策违反率等局部测试指标，无法衡量部署场景下攻击者持续适配、绕过防护后系统残留的有害输出风险，也无法横向对比不同类型防护策略的实际效果。
### 方法关键点
提出统一的部署视角评估准则，建立不同类别防护策略结果的统一映射逻辑，明确安全评估存在强证据不对称性：仅需1次成功获取有害输出的攻击即可证明风险残留，而证明风险足够低不能仅靠防护自身指标，还需验证防护执行后周边系统的风险敞口。
### 关键结果
经深度编码的现有安全评估声明中，仅极少数能提供周边系统风险敞口的有效证据，仅1份声明给出了限定范围的残余风险边界。局部防护得分提升本身不代表部署系统更安全，防护研究不能仅停留在优化局部指标，需验证全局部署后的实际安全性。
