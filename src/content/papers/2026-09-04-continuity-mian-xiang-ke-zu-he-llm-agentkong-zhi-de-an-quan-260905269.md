---
title: 'CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls'
title_zh: CONTINUITY：面向可组合LLM Agent控制的安全上下文契约框架
authors:
- Chris Zheng
- Geng Yang
affiliations:
- ZAST.AI
arxiv_id: '2609.05269'
url: https://arxiv.org/abs/2609.05269
pdf_url: https://arxiv.org/pdf/2609.05269
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: LLM Agent 可组合安全控制框架
tags:
- LLM-Agent
- Security-Control
- Composable-Contract
- Provenance-Tracking
- Access-Authorization
one_liner: 提出假设-保证契约式安全上下文验证框架，解决LLM Agent多控制组件组合时的安全断层问题
practical_value: '- 电商Agent调用支付、发券、营销消息推送等高风险工具时，可复用字段级provenance绑定+单次执行permit机制，将操作的面额、用户ID、内容等核心字段与根授权绑定，中间组件篡改值直接拦截，避免prompt
  injection导致的资损

  - 多Agent协作的推荐系统（如导购Agent、选品Agent、客服Agent串联）可复用角色绑定+假设-保证契约，明确每个Agent的输入假设、输出保证、可修改字段范围，避免上游Agent的恶意输出向下传导

  - 业务侧Agent权限治理可复用本文的7大类32种故障分类框架，覆盖根授权、溯源、组件拓扑、转换、freshness、终态、重放场景，用于设计安全合规校验用例

  - 线上部署可参考性能数据：单请求证明验证p50仅4.21ms，端到端全流程p50 7.17ms，overhead极低，适合高并发业务场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent的溯源追踪、任务级授权、策略网关等安全控制组件均独立设计测试，组合时易出现安全上下文丢失、自声明权限、权限放大、参数恶意篡改、许可重放等断层问题，仅靠数字签名无法验证组件转换操作的合法性，会导致prompt injection等攻击绕过单组件防护产生实际业务损失。
### 方法关键点
- 定义端到端后果完整性（ECI）规则：所有对外产生实际效果的操作必须携带可验证的证据链，关联根授权、主体、任务、字段级溯源、合法转换、当前策略、单次执行状态全链路信息
- 设计假设-保证契约模型：每个控制组件明确输入假设、输出保证、需保留字段、合法转换关系，上游输出必须满足下游输入假设才可流转
- 实现Continuity参考系统：支持签名根授权、角色绑定的组件身份、RFC 6901标准字段级溯源清单、带签名的转换证据、单次有效的终态执行许可，全链路校验上下文连续性
### 关键实验结果
测试集覆盖4个业务域、32种故障类、2560个攻击实例、700个正常任务、200个模糊任务。对比6种不完整控制方案，完整Continuity系统攻击成功率为0，100%自动完成正常任务，100%拦截模糊任务；最强基线方案攻击成功率达65.6%；性能上p50证明验证耗时4.21ms，端到端全流程p50耗时7.17ms。
### 核心结论
LLM Agent的安全不能依赖单组件防护，必须保障全链路安全上下文的连续性，仅靠签名和单步策略校验无法避免组合漏洞
