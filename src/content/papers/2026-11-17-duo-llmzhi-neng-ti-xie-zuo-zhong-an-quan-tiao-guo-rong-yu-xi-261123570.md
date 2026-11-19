---
title: Safe to Omit, Worth Omitting? Keeping the Answer and Cutting Latency When an
  LLM Agent Skips Another's Message
title_zh: 多LLM智能体协作中安全跳过冗余消息的低延迟推理方法
authors:
- Xinyang Li
- Chih-Hsuan Yang
- Xiaolong Ma
- Anjir Ahmed Chowdhury
- Vikram Vasudevan
- Rajeev Thakur
- Feng Yan
affiliations:
- University of Houston
- Argonne National Laboratory
- Oregon State University
arxiv_id: '2611.23570'
url: https://arxiv.org/abs/2611.23570
pdf_url: https://arxiv.org/pdf/2611.23570
published: '2026-11-17'
collected: '2026-11-19'
category: MultiAgent
direction: 多智体协作 · 低延迟推理优化
tags:
- MultiAgent
- LLM Inference
- Latency Optimization
- Risk Control
- KV Cache
one_liner: 提出基于置信度统计检验的多LLM智能体消息跳过机制，保效果同时大幅降低推理延迟
practical_value: '- 电商/搜索场景的多Agent pipeline（比如智能客服、商品问答、多阶段内容审核）可直接复用该动态跳过机制，基于接收Agent的置信度阈值筛除冗余消息，单查询可降延迟数百ms，无显著效果损失

  - 做LLM路由/级联优化时不要再依赖oracle headroom做路径选择，该指标76%的增益可由无答案相关内容的控制输入复现，参考价值极低

  - 需要保障效果稳定性的业务场景（比如广告文案生成、合规性审核）可复用文中的有限样本统计检验方法，仅用无标注流量就能校准跳过阈值，保证答案变化率不超过5%

  - 若多Agent系统采用KV cache（C2C）模式通信，跳过消息的收益远低于跳过自然语言文本消息，优先优化文本通信链路的跳过逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多LLM智能体协作场景中，接收Agent通常需要等待助手Agent的消息（文本或KV cache）才能输出结果，虽然能提升效果，但引入了显著的推理延迟瓶颈；现有基于oracle headroom的路由方法无法准确判断消息的实际价值，容易保留冗余通信。

### 方法关键点
- 定义安全跳过标准：接收Agent单独输出的答案与全链路输出的答案差异率≤5%，且跳过节省的延迟超过置信度探测的开销
- 用1次接收Agent的前向传播计算其输出置信度（1-最大答案概率）作为探测分数，无需标注数据
- 基于Learn then Test框架的有限样本二项式统计检验，在无标注校准集上自动认证最优跳过阈值，无符合要求的阈值则fallback到全链路通信

### 关键实验
在OpenBookQA、ARC-Challenge、MMLU-Pro、SQuAD等数据集上测试，覆盖多组不同参数规模的Qwen模型对、跨模型族Agent对：文本消息通信场景下可跳过59%~80%的消息，保留76%~95%的全链路效果增益，单查询平均降延迟319~1525ms；所有认证的跳过策略在unseen数据集上的答案变化率95%上界均低于5%；3智能体pipeline场景下可跳过39.9%的验证Agent消息，保留12.55/12.80的效果增益，单查询降延迟483ms。

最值得记住的结论：多智能体通信的可跳过性取决于消息改变接收端答案的频率和可预测性，和消息本身的整体准确率无关。
