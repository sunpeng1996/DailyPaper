---
title: 'Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming'
title_zh: Agent攻击Agent：面向生产级Agent红队测试的自动研究框架
authors:
- Xutao Mao
- Xiang Zheng
- Cong Wang
affiliations:
- City University of Hong Kong
arxiv_id: '2607.11698'
url: https://arxiv.org/abs/2607.11698
pdf_url: https://arxiv.org/pdf/2607.11698
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: Agent 生产环境安全红队测试
tags:
- Red-Teaming
- LLM Agent
- Vulnerability Discovery
- Falsifiable Hypothesis
- VCG
one_liner: 提出可证伪的自动红队框架AHA，产出可复用可审计的漏洞概念图，较最优基线成功率提升14.2个百分点
practical_value: '- 自研业务Agent（电商客服、推荐调度、广告运营类Agent）可复用AHA的可证伪红队流程，先明确漏洞假设和证伪规则再构造攻击，避免无效随机渗透，产出的VCG可直接作为安全补丁的回归验证用例库

  - VCG的结构化设计（漏洞声明、触发条件、攻击模板、证伪规则）可迁移到电商/推荐业务规则漏洞挖掘场景，比如薅羊毛漏洞、广告投放规则绕过、推荐流量作弊的自动化挖掘，把零散漏洞Case沉淀为可复用的机制知识

  - 跨场景/跨模型的单-shot漏洞迁移验证思路，可用于业务Agent的版本迭代测试：大模型升级、工具链更新后，直接用历史VCG做无额外搜索的单轮测试，大幅降低回归测试的攻击构造成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
当前生产级LLM Agent（如代码生成Agent、业务调度Agent）的安全故障会直接触发文件写入、数据泄露、业务流程异常等真实操作风险，传统红队工具仅留存攻击payload，不记录漏洞触发的根因条件，场景/模型更新后即失效，也无法支持审计、补丁验证等生产运维需求。
## 方法关键点
1. 设计AHA可证伪自动红队循环，严格遵循「先提出漏洞假设+明确证伪规则→基于假设构造场景合法的攻击→沙箱执行攻击并采集全轨迹→对比轨迹验证假设→定期审计反作弊」的流程，避免后验解释和奖励作弊。
2. 提出VCG（Vulnerability Concept Graph）结构化存储经过验证的漏洞知识，每个节点包含漏洞声明、触发条件、攻击模板、故障结果、迁移预测、证伪规则等字段，仅满足≥3次验证、≥60%成功率的漏洞才会进入正式VCG。
3. 采用严格的「发现阶段冻结VCG→测试阶段单-shot无额外搜索」的评估协议，排除测试时搜索优化的干扰，真实衡量漏洞知识的复用性。
## 关键结果
在Claude Code、Codex两个生产Agent，AgentHazard、AgentDyn、DTap三个红队场景，Minimax、Kimi、Deepseek三个大模型上测试：冻结VCG的单-shot攻击成功率平均达47.0%，较最优冻结基线高14.2个百分点；漏洞概念跨场景、跨模型迁移的平均攻击成功率达原生场景的88%，可在不同模型、攻击渠道间复用。
## 核心结论
红队的核心产出不应是一次性的攻击payload，而是可审计、可复用的漏洞机制知识，后者才是能随产品迭代持续积累的安全基础设施
