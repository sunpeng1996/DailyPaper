---
title: 'AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents'
title_zh: AutoPI：分类体系引导的LLM Agent提示注入自适应红队框架
authors:
- Stavros Damianakis
- Konstantinos Psounis
affiliations:
- University of Southern California
arxiv_id: '2611.24313'
url: https://arxiv.org/abs/2611.24313
pdf_url: https://arxiv.org/pdf/2611.24313
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: LLM Agent 提示注入红队测试优化
tags:
- Red Teaming
- Prompt Injection
- LLM Agent
- Black-box Attack
- Coverage-aware Evaluation
one_liner: 基于提示注入分类体系的黑盒无训练自适应红队，兼顾攻击成功率与技术覆盖度
practical_value: '- 可复用「分类体系引导探索+局部反馈优化」框架，用于电商导购Agent、推荐交互Agent的内部安全测试，覆盖更多对抗样本类型，避免对抗训练只拟合少数攻击模式

  - 黑盒无训练的测试方案可直接迁移，不需要获取模型权重/梯度，适合对接内部闭源Agent做对抗性鲁棒性验证，降低测试成本

  - 可参考「攻击成功率+技术覆盖度」双指标评估体系，替代单一通过率的安全测试，更准确衡量Agent对抗未知注入攻击的鲁棒性

  - 用该框架生成的多样化注入样本做对抗训练数据，能提升模型对未知攻击类型的泛化防御能力，避免窄样本训练导致的防御漏洞'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
提示注入是LLM Agent当前排名第一的未解决安全风险，现有自适应红队工具大多仅优化攻击成功率（ASR），倾向复用少数有效攻击技术，导致测试覆盖不全；基于固定模板的基准测试会严重高估模型鲁棒性，对抗训练使用的单一攻击样本也会遗留大量安全漏洞。
### 方法关键点
- 以PIATLAS提示注入技术分类体系（6大类、34种技术、132种子技术）为搜索引导，将技术覆盖度作为与ASR并列的核心评估指标
- 采用黑盒无训练的三段式流程：可选固定种子初始化→遍历分类体系所有子技术生成对应场景专属注入prompt的探索阶段→基于LLM裁判反馈优化失败注入的 exploitation 阶段
- 支持灵活调整策略，可选择侧重ASR的种子优化模式，或侧重覆盖度的全分类遍历模式，适配不同测试需求
### 关键结果
在AgentDojo、IPI Arena两个基准上测试，对比PIMiner、CtH、AutoDojo三类SOTA自适应红队工具：
1. 针对Qwen3.6-35B，AutoPI全量模式覆盖90%以上PIATLAS技术，基线最高仅为65%
2. 针对最鲁棒的Claude Haiku 5.5，ASR比基线高20%~50%，类级别覆盖度高25%~400%
3. 无需预训练的种子优化模式ASR排名第二，仅低于需预训练的CtH，单尝试成本仅为基线的1/2.4~1/24

**最值得记住的一句话**：LLM Agent的鲁棒性是最坏-case属性，仅测试已知攻击模式会严重高估安全性，高覆盖度的红队测试比单纯高攻击成功率更能暴露真实风险
