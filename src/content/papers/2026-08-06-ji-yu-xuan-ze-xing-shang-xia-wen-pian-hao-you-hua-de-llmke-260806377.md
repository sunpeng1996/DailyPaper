---
title: Learning When to Trust via Selective Context Preference Optimization
title_zh: 基于选择性上下文偏好优化的LLM可信上下文判断方法
authors:
- Xian Sun
- Wei Chow
- Yingshuo Wang
- Junhao Liu
- Wei Gao
- Qing Wu
- Lingdong Kong
affiliations:
- Duke University
- National University of Singapore
- UC Berkeley
- UC Irvine
- Northeastern University
arxiv_id: '2608.06377'
url: https://arxiv.org/abs/2608.06377
pdf_url: https://arxiv.org/pdf/2608.06377
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: LLM对齐 · 选择性信任与偏好优化
tags:
- DPO
- Preference Optimization
- LLM Robustness
- Benchmark
- Context Trust
one_liner: 提出衡量LLM选择性信任的MIST基准与SCOPE偏好训练法，降低误导干扰同时保留上下文利用能力
practical_value: '- 电商RAG搜索/商品问答场景可复用SCOPE的四元组平衡训练思路，将干净query、正确检索结果、无关检索结果、误导检索结果的偏好对等权重加入DPO训练，避免模型为了抗干扰忽略有用的商品参数/评价信息

  - 推荐Agent/导购Agent的效果评估可引入MIST的四元组测试范式，构造业务场景测试集，用SC2W指标衡量Agent被错误工具返回、用户误导性输入带偏的概率，替代单一准确率指标，更精准定位鲁棒性问题

  - 电商客服LLM微调时，可复用SC2W指标筛选容易被错误用户query、误导性评论带偏的bad case，针对性构造偏好训练对，降低错误应答、答非所问的概率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM极易被合理的误导性上下文翻转正确答案，而单纯训练抗干扰能力会导致模型一刀切忽略所有外部上下文，无法利用正确的辅助信息；现有基准仅测评单一上下文下的准确率，无法区分「选择性信任有效信息」和「全盘拒绝所有上下文」两种行为，无法支撑鲁棒且实用的推理模型优化。

### 方法关键点
- 构建MIST人类标注基准：每个推理问题对应4组完全匹配的上下文变体（无额外上下文、误导性上下文、正确辅助上下文、无关上下文），问题、答案空间、金标准完全一致，仅上下文不同；新增SC2W指标，衡量模型在干净问题上答对、加误导上下文后答错的比例，精准隔离误导信号带来的错误。
- 提出SCOPE训练框架：挖掘基模型「干净答对+误导答错」的失败case，构造同一问题下<符合事实的正确应答、跟随误导的错误应答>偏好对，将4种上下文的偏好对按等权重加入标准DPO训练，不修改DPO损失函数，仅优化训练数据的分布平衡。

### 关键结果
覆盖23款开源/闭源LLM的测试显示，误导信号会带来平均17.1个点的准确率下降；SCOPE在Qwen3-4B上将SC2W从35.0降至16.3，在Llama-3.2-3B上从31.5降至20.6，同时保持甚至提升干净、正确上下文、无关上下文下的准确率，效果零样本迁移到GSM-IC、GSM-Plus等3个外部基准。

> 最值得记住的一句话：可靠的推理模型应该基于选择性信任来训练和评估，而非单纯追求抗干扰能力。
