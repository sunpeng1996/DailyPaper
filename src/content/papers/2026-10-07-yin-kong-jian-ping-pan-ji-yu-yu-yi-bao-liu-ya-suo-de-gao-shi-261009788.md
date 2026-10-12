---
title: 'Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving
  Compression'
title_zh: 隐空间评判：基于语义保留压缩的高效生成式奖励建模
authors:
- Mingqing Yuan
- Xiaobo Liang
- Junwei Yang
- Ziwei Chen
- Zeren Zhang
- Hejin Wang
- Yubin Wang
- Juntao Li
affiliations:
- Soochow University
- University of Cambridge
- Chalmers University of Technology
- Peking University
- Tsinghua University
arxiv_id: '2610.09788'
url: https://arxiv.org/abs/2610.09788
pdf_url: https://arxiv.org/pdf/2610.09788
published: '2026-10-07'
collected: '2026-10-12'
category: LLM
direction: LLM对齐 · 高效生成式奖励建模
tags:
- Reward Model
- Latent Reasoning
- Semantic Compression
- Inference Optimization
- Generative Reward Model
one_liner: 提出LatentGRM隐空间奖励建模框架，在保留判断准确率前提下将推理速度提升6.1-7.0倍
practical_value: '- 生成式推荐/Agent的多维度质量校验场景可复用语义分块思路，以商品合规、内容相关性、用户偏好匹配等评价规则为锚点压缩推理链，降低多轮打分成本

  - 高吞吐奖励打分场景（如推荐大模型RLHF对齐、批量内容审核）可直接借鉴两阶段蒸馏架构，用显式SFT打分模型做教师，蒸馏出的隐空间打分模型推理速度提6倍以上，精度损失可忽略

  - 需可解释性的评价场景可复用Latent Trace Interpreter设计，在线路径用隐式快速打分，离线从隐轨迹重建完整评价理由，平衡效率和可解释性要求

  - 工程上可参考其vLLM扩展方案，支持软嵌入反馈的连续批处理、KV cache复用，降低隐式生成部署开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前生成式奖励模型依赖生成显式推理链完成多维度评价，推理成本极高，尤其在需要多次投票、批量打分的RLHF、内容审核、推荐结果质量校验等场景，成本压力尤为突出；现有隐式推理方法未适配奖励建模的结构化评价规则，难以保证核心语义信息不丢失。

### 方法关键点
- 语义分块：基于评价规则（rubric）结构划分语义块，分配固定隐向量预算，再结合句法边界优化分块位置，避免拆分完整语义单元，效果优于固定比例分块
- 两阶段蒸馏：第一阶段将显式SFT教师模型的评价推理链蒸馏为连续隐向量序列；第二阶段训练模型自主生成隐向量序列并直接输出偏好结果，无需生成显式文本
- 隐轨迹解释器：单独训练离线解释器，可从保存的隐向量序列重建完整评价理由文本，不占用在线推理资源

### 关键结果
基于Qwen3 4B/8B backbone，用3.5万条OpenRubrics数据训练，和同等数据、同等大小的显式SFT奖励模型对比：8个benchmark上vote@5平均准确率高0.9pp；8B版本在4个核心benchmark上推理轨迹压缩8.9-9.2倍，vLLM部署下推理速度提升6.1-7.0倍；隐轨迹解释器重建评价状态的Macro-F1达98.93%，重建的评价理由用于下游内容优化的效果甚至优于显式生成的理由。

结构化语义引导的隐空间压缩可以在几乎不损失效果的前提下，将依赖长推理链的生成式评价任务推理成本降低一个数量级，同时保留可解释性回溯能力。
