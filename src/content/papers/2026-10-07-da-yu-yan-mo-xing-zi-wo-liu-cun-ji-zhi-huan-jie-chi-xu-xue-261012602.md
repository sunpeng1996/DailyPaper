---
title: Self-Preservation in Language Models
title_zh: 《大语言模型自我留存机制：缓解持续学习中的灾难性遗忘》
authors:
- Dongkyu Cho
- Rumi Chunara
- Ali Behrouz
affiliations:
- New York University
- Google Research
- Cornell University
arxiv_id: '2610.12602'
url: https://arxiv.org/abs/2610.12602
pdf_url: https://arxiv.org/pdf/2610.12602
published: '2026-10-07'
collected: '2026-10-12'
category: Training
direction: LLM持续学习 · 自生成回放抗遗忘
tags:
- Continual Learning
- Catastrophic Forgetting
- Replay
- Instruction Tuning
- Self-Preservation
one_liner: 提出基于Task Bank的自生成回放框架，可在无原始训练数据时缓解LLM微调的灾难性遗忘
practical_value: '- 业务场景中对LLM做领域微调（如电商客服/推荐文案生成模型新增行业知识）时，可采用Task Bank自生成回放方案，无需存储原始训练数据就能减少原有能力的遗忘，避免新功能上线后旧功能失效

  - LLM微调超参选择时不要仅关注新任务准确率，需新增Retention（原有正确样本训练后仍正确的比例）指标监控，避免平均准确率掩盖旧能力的实际损失，比如微调query生成模型时要验证原有热门query的生成效果是否下降

  - 若使用≥4B规模的LLM做领域适配，可引入新任务感知的回放目标选择策略，相比随机选择能提升2~3pp的旧能力留存率，同时新任务效果几乎无损

  - LLM微调优先选择较低学习率，实验显示Qwen3-1.7B用1e-7学习率比1e-5的新任务增益高14.06pp，同时旧能力留存率高64.14pp，可直接参考作为调参基线'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大语言模型预训练成本极高，微调适配新领域/新任务时容易发生灾难性遗忘；传统回放方法依赖原始训练数据，但业务场景中原始数据往往因版权、存储成本不可用，仅靠有限留存任务做回放无法覆盖模型全部原有能力，且平均准确率指标会掩盖旧能力的实际损失。

### 方法关键点
- 构建**Task Bank**：存储任务描述和少量示例，无需原始训练数据
- 自生成回放：用冻结的预更新模型为选中的Task Bank条目生成回放样本，和新任务样本混合做SFT
- 三类目标选择策略：随机选择、仅基于Task Bank选择、新任务信息感知选择
- 新增**Retention**指标：统计原有正确样本训练后仍正确的比例，更精准衡量遗忘程度

### 关键结果
基于0.6B/1.7B/4B三个尺寸的Qwen3模型做指令微调，新任务为MedQA/C-STANCE，4个任务入Task Bank，4个任务作为held-out集测试泛化能力，对比SFT、真实样本回放等baseline：
1. 组合两个半区Task Bank，在0.6B/1.7B/4B上分别比单个半区Bank提升4.42/3.32/2.99pp的held-out Retention，新任务增益仅降0.28~0.6pp
2. 4B模型用新任务感知选择策略，比随机选择提升2.75pp的held-out Retention，新任务增益几乎无损失，小模型无此收益
3. 1.7B模型用1e-7学习率比1e-5学习率，新任务增益高14.06pp，held-out Retention高64.14pp

> 最值得记住的结论：LLM微调时不要只看新任务准确率，监控旧能力正确样本的留存率、用自生成回放补充保护，能以极小的新任务效果损失大幅降低灾难性遗忘的风险
