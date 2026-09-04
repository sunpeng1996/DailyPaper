---
title: The Implications of Linguistic Illegibility for LLM Security
title_zh: 语言不可读性对大语言模型安全的影响
authors:
- James Mickens
affiliations:
- Harvard University
arxiv_id: '2609.02852'
url: https://arxiv.org/abs/2609.02852
pdf_url: https://arxiv.org/pdf/2609.02852
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: 大语言模型安全 · 沙箱防护机制
tags:
- LLM-Security
- Sandbox
- Taint-Tracking
- Chain-of-Thought
- Activation-Probing
one_liner: 提出LLM语言不可读性概念，论证依赖语言自报告的安全机制不可靠，给出不依赖语言的沙箱防护方案
practical_value: '- 搭建基于Agent的电商推荐/广告系统时，不得仅依赖CoT输出、模型自审查做安全校验，必须额外增加独立隔离层，避免prompt注入等攻击绕过语言层面校验

  - 落地Agent业务接口权限管控时，可借鉴taint tracking思路，预先定义禁止被模型输出修改的核心系统状态（如用户支付状态、商品库存字段），从数据流层面做拦截

  - 用LLM做生成式推荐文案、query改写时，不要通过探测模型激活层语言特征做合规校验，这类机制存在固有被绕过风险，优先用独立外部内容审核服务'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM安全方案多依赖模型语言输出、激活层语言特征探测判断内部逻辑，无法可靠应对prompt注入、沙箱逃逸等攻击，存在固有缺陷。
### 方法关键点
1. 提出**语言不可读性**概念：LLM内部计算基于激活空间的数学运算，和自然语言转换存在固有损失，外部语言产物（输出、可探测语言特征）无法100%反映真实计算逻辑，该问题不可彻底消除。
2. 论证所有依赖语言自报告的安全机制（CoT监控、宪法式自审查、语言特征激活探测）均不可能完全可靠，无法作为唯一安全防线。
3. 给出兜底防护方案：以污点跟踪为核心，预先定义禁止被模型输出修改的系统状态，辅以强虚拟化、沙箱配置第三方审计等不依赖语言状态的隔离机制。
### 关键结果
这套不依赖语言监控的防护体系可缓解近期前沿模型出现的各类沙箱逃逸漏洞，为LLM落地提供基础安全兜底
