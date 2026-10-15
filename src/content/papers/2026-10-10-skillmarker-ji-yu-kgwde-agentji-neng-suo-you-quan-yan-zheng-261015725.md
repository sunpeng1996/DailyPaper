---
title: 'SkillMarker: A KGW-Based Watermarking Method for Agent Skill Ownership Verification'
title_zh: SkillMarker：基于KGW的Agent技能所有权验证水印方法
authors:
- Alan Tang
- Lifeng Wang
- Gang Wu
- Tao Zhang
- Yantao Jia
- Xiaofeng Zhu
affiliations:
- Huawei Technologies Co., Ltd.
- Harbin Institute of Technology, Shenzhen
arxiv_id: '2610.15725'
url: https://arxiv.org/abs/2610.15725
pdf_url: https://arxiv.org/pdf/2610.15725
published: '2026-10-10'
collected: '2026-10-15'
category: Agent
direction: Agent技能安全 · 水印技术
tags:
- Agent
- Watermarking
- KGW
- Ownership Verification
- Skill Protection
one_liner: 基于KGW架构提出兼顾功能保留与强鲁棒性的Agent技能水印方案，支持所有权验证与泄露溯源
practical_value: '- 电商/广告Agent的核心技能（如投放策略、运营自动化流程、客服标准化话术）可直接复用该框架，将代码、参数阈值、API标识符设为保护段，仅重写非核心描述段嵌入水印，防止核心知识资产被盗用

  - 水印检测可复用滑动窗口方案，无需模型推理，仅需tokenizer和密钥即可批量审计技能资产，快速定位泄露片段

  - 重写阶段的保真prompt规则（保留原意、数值、条件、技术标识符）可迁移到所有需语义不变的文本改写场景，如推荐话术同义生成、广告文案变体生产

  - 水印嵌入的token变体分组、格式token豁免trick可直接复用，避免水印改写破坏结构化文档（如Markdown格式的策略手册、API文档）的可用性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Agent技能是封装了领域知识、操作流程的可复用资产，明文分发易被非法复制、二次分发，但现有水印方案无法适配技能指令的强准确性要求：微小改动就可能导致逻辑错误、功能失效，同时结构化的紧凑指令留给改写的空间极小，难以嵌入足够强的水印信号。

### 方法关键点
- 质量约束重写：先拆分技能为**保护段**（代码、API标识符、数值阈值、结构分隔符）和可编辑段，仅对可编辑段改写；prompt加入明确保真规则和示例，确保改写不改变指令逻辑、条件、数值
- 适配KGW水印逻辑：对Markdown格式token、特殊控制token豁免logit bias，仅差异为前导空格/点的同类token变体共享绿名单归属，避免破坏结构化格式
- 信号导向候选搜索：对可编辑段用beam搜索生成多个改写候选，按绿token率优先、低PPL兜底的规则选最优，在保真前提下最大化水印信号
- 检测支持全文本和滑动窗口两种模式，无需模型推理，仅需密钥和tokenizer即可完成所有权验证和泄露片段定位

### 关键实验结果
在4个覆盖通用、开发、营销、专业技能的数据集上验证：
- 水印后技能的下游任务性能波动仅为**-2.01%~+0.93%**，几乎无功能损失
- 复制粘贴场景下，仅需**1536个连续token的片段即可100%检测到水印**，定位召回达98.0%~99.1%
- 技能合并场景下，和1/3个背景技能合并后，水印检测率仍保持**72.2%~77.8%**

最值得记住的一句话：结构化知识资产的水印嵌入核心是在保真约束的极小改写空间里最大化水印信号，而非无限制改写文本。
