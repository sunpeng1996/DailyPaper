---
title: 'Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming'
title_zh: AI-Infra-Guard：面向AI Agent的多层级安全红队测试开源框架
authors:
- Yong Yang
- Xing Zheng
- Huiyu Wu
- Huangsheng Cheng
- Xiaorong Shi
- Jing Guo
- Bo Yang
- Yi Zhou
- Xiangfan Wu
- Zonghao Ying
affiliations:
- Tencent Zhuque Lab
arxiv_id: '2606.31227'
url: https://arxiv.org/abs/2606.31227
pdf_url: https://arxiv.org/pdf/2606.31227
published: '2026-06-29'
collected: '2026-07-06'
category: Agent
direction: Agent安全 · 多层红队测试框架
tags:
- Agent Security
- Red Teaming
- LLM Security
- MCP
- Supply Chain Security
one_liner: 基于层-范式匹配原则打造开源全栈AI Agent安全红队测试框架，覆盖4层攻击面
practical_value: '- 业务Agent安全校验可直接复用分层检测思路：基础设施层用规则快速扫描已知漏洞，工具/行为层用LLM驱动的智能审计，模型层用越狱测试库校验对齐能力，覆盖率远高于单一检测方案

  - Prompt-as-Rule范式可直接复用在业务自定义风险检测：将电商/推荐场景的违禁内容、合规要求写成自然语言规则喂给LLM审计器，无需硬编码正则，适配迭代快的业务规则

  - 引入第三方Agent插件/工具时，可直接复用静态+动态审计流程，排查投毒、越权、隐式prompt注入风险，规避供应链漏洞

  - 线上业务Agent安全测试可复用成本可控的黑盒红队设计：采用escalation阶梯、停止规则、金丝雀token验证，平衡风险覆盖度和调用成本，避免影响线上服务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI Agent生态迭代速度远超安全工具迭代速度，传统安全工具存在三大缺陷：主流指纹库未收录主流AI组件、AI项目不规则版本号（如build号、dev快照、latest标签）导致传统版本匹配逻辑失效、传统Web漏洞扫描器针对注入、XSS等缺陷设计，无法覆盖AI场景核心风险（未授权GPU访问、凭证泄露、prompt注入、工具滥用、模型对齐失效），且风险分布在基础设施、协议/工具、Agent行为、模型四个完全不同的抽象层，单一检测范式无法实现全栈覆盖。

### 方法关键点
- 核心采用**层-范式匹配**原则：为每层攻击面匹配成本最低、效果最优的检测范式，避免用单一技术适配所有场景
- 基础设施层：用声明式规则匹配引擎，覆盖75+AI组件、1443条漏洞规则，自研版本归一化逻辑适配不规则版本号，扫描速度快、可复现、误报率接近0
- 协议/工具层：采用LLM驱动的Agent审计框架，支持静态代码审计+动态黑盒调用双模式，首创Prompt-as-Rule范式，将漏洞检测规则编码为自然语言，可快速适配新风险，内置间接prompt注入防护逻辑避免审计器本身被攻击
- Agent行为层：采用成本可控的多轮黑盒红队测试，通过escalation阶梯、停止规则、金丝雀token验证平衡覆盖度和调用成本
- 模型层：内置26+攻击算子、16个红队数据集的越狱测试框架，用LLM-as-judge自动判断攻击成功率，量化模型对齐鲁棒性

### 关键结果
目前唯一覆盖AI全栈4层攻击面、同时支持Agent技能供应链审计的开源框架，基础设施层覆盖75+主流AI组件、1443条漏洞规则，模型层内置26+攻击算子、16个红队数据集，可直接开箱使用。

### 核心结论
不存在依赖单一检测范式的通用扫描器可以覆盖现代AI全栈的安全风险，分层适配检测范式是兼顾效率和覆盖度的最优方案。
