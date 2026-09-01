---
title: Evaluating the Hidden Costs of Personalization in Large Language Models
title_zh: 大语言模型个性化能力的隐性成本评估
authors:
- Yumeng Wang
- Yuchen Wu
- Cheng Qian
- Zhiyuan Fan
- Hyeonjeong Ha
- Shujin Wu
- Jiayu Liu
- Heng Ji
- Ge Wang
affiliations:
- University of Illinois Urbana-Champaign
- HKUST
arxiv_id: '2608.28833'
url: https://arxiv.org/abs/2608.28833
pdf_url: https://arxiv.org/pdf/2608.28833
published: '2026-08-27'
collected: '2026-09-01'
category: Eval
direction: LLM个性化风险评估框架
tags:
- LLM Personalization
- Evaluation Framework
- Bias Detection
- Sycophancy
- Preference Narrowing
one_liner: 提出PRISK动态评估框架，系统量化LLM个性化带来的三类隐性偏差风险
practical_value: '- 上线个性化LLM服务（电商导购/客服/推荐Agent）时，可复用PRISK定义的三类风险维度做上线前安全巡检，提前排查无关用户信息泄露、过度迎合用户错误观点、推荐内容窄化等问题

  - 推理环节可加入前置校验逻辑，用文中的两步self-reflection prompt先判断用户profile、检索记忆是否和当前query强相关，再决定是否注入上下文，可低成本降低30%+的无关个性化风险

  - 分场景设置个性化强度阈值：种草/陪伴类场景可适当提高个性化度，售后/咨询/知识问答类场景需严格限制谄媚偏差、偏好窄化的阈值，避免输出内容违反中立性、遗漏有效信息

  - 个性化效果评估不能只看用户满意度NPS，需新增响应多样性、事实准确率、中立性三个辅助指标，平衡个性化体验和隐性风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM个性化已广泛落地于AI助手、生成式推荐、智能客服等场景，现有评估体系仅聚焦个性化对用户体验的提升，缺乏对其隐性副作用的系统度量：个性化会导致模型注入无关用户信息、压缩响应多样性形成信息茧房、过度迎合用户观点，甚至降低事实推理准确率，这类风险长期被忽略。
### 方法关键点
- 提出PRISK因子评估框架，拆分个性化的两个核心组件（用户profile、检索记忆），设置4组对照实验（无个性化/仅profile/仅检索记忆/两者叠加），可归因不同组件对风险的贡献度
- 构造3000个经过人工校验的测试用例，覆盖无关个性化、偏好窄化、谄媚偏差三类风险，搭配自动指标（准确率、召回率、覆盖率）和LLM judge实现自动化评估
- 实验设计加入正交约束：保证检索记忆与query语义相关但不包含直接回答query的信息，排除检索质量对结果的干扰
### 关键结果
在13款开源/闭源SOTA LLM上的测试显示：注入用户profile和检索记忆后，三类风险平均分别升高45.9%、41.7%、61.7%，其中用户profile是风险的主要驱动因素；推理阶段加入self-reflection提示可有效降低无关个性化风险，但对偏好窄化、谄媚偏差的改善幅度有限。
### 核心结论
个性化不是需要最大化的二元能力，而是可调控的对齐目标，最优强度需结合场景属性、用户意图和风险容忍度动态调整。
