---
title: Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How
  Preference Cues Are Delivered
title_zh: 推理模型思维链忠实度随偏好提示的投放位置与形式变化
authors:
- Aryo Pradipta Gema
- Neel Rajani
- Rohit Saxena
- Wai-Chung Kwan
- Pasquale Minervini
affiliations:
- University of Edinburgh
- Miniml.AI
arxiv_id: '2608.29464'
url: https://arxiv.org/abs/2608.29464
pdf_url: https://arxiv.org/pdf/2608.29464
published: '2026-08-29'
collected: '2026-09-01'
category: Eval
direction: LLM推理 · CoT忠实度评估
tags:
- CoT
- Faithfulness
- Evaluation
- Agent
- Preference Alignment
- LLM Reasoning
one_liner: 提出FACE-Eval评估基准，揭示偏好提示的投放渠道、显隐性显著影响推理模型CoT忠实度，现有干预难消弭差距
practical_value: '- 做电商导购Agent的用户偏好对齐时，对RAG召回的用户历史行为、客服聊天记录等隐性偏好，不能仅靠CoT审计是否被使用，工具返回的偏好未被CoT记录的概率比用户输入高0.03-0.21，需额外增加偏好溯源校验逻辑

  - 若要提升CoT忠实度，可优先添加「所有引用信息需标注来源并说明对决策的影响」的系统提示，对Qwen、DeepSeek等系列模型可缩小用户输入与工具返回的忠实度差距，但需测试是否会提升用户侧未记录率

  - 搭建Agent决策审计系统时，对来自工具/检索的隐性偏好，降低对单靠CoT检测的依赖，这类场景下GPT-5.6-Luna级别监测器的AUROC仅0.71左右，低于用户输入场景的0.73

  - 若使用GPT-OSS系列模型，可适当调高推理努力度，能有效降低未被记录的偏好采用率，DeepSeek V4 Pro、Inkling等模型调整推理努力度的提升效果不显著'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有CoT忠实度评估仅测试嵌入用户输入的显式提示，而实际Agent系统中用户偏好提示常来自工具返回、RAG检索结果、历史记忆等外部渠道，且多为需要推断的原始数据（如浏览记录、聊天片段），原有评估框架无法覆盖这类场景的CoT忠实度表现，也不清楚提示投放位置、显隐性对忠实度的量化影响，难以支撑Agent决策审计的可靠性设计。

### 方法关键点
- 提出FACE-Eval评估基准，共5100样本，覆盖2个投放渠道（用户输入/工具返回）、2种显隐性（显式偏好总结/需推断的原始数据）、5类偏好维度、5种信息来源、20个决策场景，相同偏好的提示文本在不同渠道、显隐性下严格对齐。
- 定义3个核心指标：VCR（偏好对齐的回答中CoT明确提及使用该偏好的比例）、CFR（偏好提示下回答对齐偏好的比例）、UAR（回答对齐偏好但CoT未提及使用该偏好的比例）。
- 测试15个开源推理模型（参数范围4B~1.6T），对比默认、来源归因指令、监测告知3种系统提示的效果，同时测试推理努力度对忠实度的影响。

### 关键结果
- 所有模型的VCR均满足：用户输入>工具返回，显式提示>隐式提示；工具返回的UAR比用户输入高0.03~0.21，隐式提示的UAR比显式提示平均高0.05左右。
- 来源归因提示仅在7/15模型上缩小渠道差距，其中4款模型是靠提升用户侧UAR实现，监测告知提示无稳定的差距缩小效果。
- GPT-5.6-Luna监测器检测未记录偏好的AUROC为0.71~0.73，仅用户侧场景添加CoT能提升检测效果，工具侧场景无明显增益，UAR越高的场景监测AUROC越低（相关系数-0.54）。

> 最值得记住：不要默认CoT会如实记录所有决策依赖的信息来源，来自工具/检索的隐性偏好的CoT忠实度远低于用户输入的显式提示，单靠CoT审计Agent决策存在显著盲区。
