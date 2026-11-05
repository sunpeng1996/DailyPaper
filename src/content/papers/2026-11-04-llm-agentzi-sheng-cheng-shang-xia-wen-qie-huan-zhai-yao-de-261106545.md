---
title: When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written
  Handoff Summaries
title_zh: 《LLM Agent自生成上下文切换摘要中的无依据权限规则研究》
authors:
- Wenhui Chu
affiliations:
- University at Albany, State University of New York
arxiv_id: '2611.06545'
url: https://arxiv.org/abs/2611.06545
pdf_url: https://arxiv.org/pdf/2611.06545
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent上下文压缩 · 权限安全优化
tags:
- LLM Agent
- Memory Compaction
- Handoff Summary
- Policy Hallucination
- Agent Safety
one_liner: 量化LLM Agent切换摘要的无依据权限规则问题，提供仅改一行提示词的低成本修复方案
practical_value: '- 部署长周期业务Agent（如电商智能运营、客服Agent）时，避免使用模糊的权限类系统提示词，替换为明确的权限来源说明，无需额外开发成本即可将无依据权限限制降低80%以上，且不影响正常审批请求

  - 做Agent上下文压缩模块时，除了事实一致性校验，新增权限规则校验：对比摘要中的权限表述与真实权限账本，移除无依据授权语句，可将未授权操作风险降低70%

  - 高权限业务Agent可采用低成本加固方案：上下文切换时将当前真实权限列表追加到生成的摘要末尾，无需修改摘要内容即可大幅降低权限违规概率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长周期LLM Agent依赖上下文压缩（生成切换摘要）解决上下文窗口不足问题，过往研究仅关注压缩导致的信息丢失，未发现摘要会主动生成无依据的权限规则，这一问题会导致后续Agent执行违规操作，对涉及改价、发券、数据修改等敏感操作的电商/运营类Agent会带来直接业务风险。
### 方法关键点
- 构建三类合成工具任务（记录管理、报告发布、代码修改），自带独立于Agent的ground truth权限账本和事件日志，覆盖常见权限校验场景
- 提出same-snapshot replay因果验证方法：在同一环境快照下，将摘要中可疑权限句子替换为无意义中立填充词，对比后续Agent的行为差异，隔离目标句子的影响
- 标注两类无依据政策：无依据限制（要求规则未规定的审批）、无依据授权（声称未获批操作可执行），用双AI reader标注确保准确性
### 关键结果
- 两款开源模型Qwen3-8B、gpt-oss-20B的可阅读摘要中，无依据限制占比1.2%~2.4%，无依据授权占比0.1%~1.3%
- 移除无依据授权句子可将未授权操作从24/120降至7/120，风险降低70%+
- 将系统提示词中模糊的"Some actions need approval"替换为明确的"仅规则或用户请求指定的操作需要审批"，无依据限制在开发集从5.0%降至1.8%，测试集从1.8%降至0.3%，正常审批请求几乎无变化
### 核心结论
Agent自生成的记忆摘要不仅会丢失信息，还会主动 hallucinate 不存在的权限规则，仅修改一行系统提示词即可大幅降低此类风险。
