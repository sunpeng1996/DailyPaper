---
title: Is Token Confidence Just Chain Length? A Signal-Processing Audit of Reasoning
  Traces
title_zh: Token置信度本质是推理链长度？基于信号处理的推理轨迹审计
authors:
- Pragna Mallappa
affiliations:
- Keshav Memorial Institute of Technology
arxiv_id: '2610.36709'
url: https://arxiv.org/abs/2610.36709
pdf_url: https://arxiv.org/pdf/2610.36709
published: '2026-10-27'
collected: '2026-10-28'
category: Reasoning
direction: LLM推理 · 置信度评估 效率优化
tags:
- Chain-of-Thought
- Token Confidence
- Signal Processing
- Self-Consistency
- Reasoning Efficiency
one_liner: 用信号分析证实基于token置信度的推理链筛选本质是测链长，额外信号弱到无法提效
practical_value: '- Agent推理/导购类业务做自洽性优化时，无需实现复杂的滑动窗口置信度筛选逻辑，直接优先选择短推理链即可，开销更低且效果不逊色于置信度方案

  - 推理链早期停止场景下，直接减少采样链数的方案比所有基于置信度的停止规则的成本收益比更高，能有效降低高并发场景下的token开销和推理时延

  - 后续做任何基于token置信度的LLM相关优化（如推荐文案质量校验、搜索query改写正确性判断）时，必须加入链长作为基线，避免将长度效应误判为置信度的贡献

  - 若需要更精细的推理质量校验，可尝试引入高频段频谱能量特征作为补充特征，适合对准确率要求较高的业务场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
基于多链多数投票的自洽性推理能显著提升LLM数学题准确率，但多链生成会带来极高的token开销。此前业界提出的DeepConf方法通过滑动窗口统计token置信度筛选推理链以降本，但该置信度信号的实际价值和底层逻辑从未被系统性拆解，存在将混淆效应误判为有效信号的风险。

### 方法关键点
- 将逐token置信度序列视为离散时间信号，用频谱分析、突变检测等经典信号处理工具拆解其组成
- 对比不同滤波窗口（boxcar、Hann、指数移动平均）、池化规则的筛选效果，以及CUSUM突变检测器的早期停止效果
- 设计长度移除AUROC指标，剥离链长的影响后单独评估置信度信号的真实判别能力

### 关键结果
实验基于DeepSeek-R1-Distill-Qwen-1.5B模型，在MATH500（200题）、GSM8K（300题）基准上每题采样16条推理链：
1. 按链长从短到长排序选链的AUROC在MATH500达0.715，比DeepConf的2048窗口方案高0.13；在GSM8K达0.636，与DeepConf持平
2. 移除链长影响后，DeepConf的AUROC降至0.486~0.52，完全为随机水平，无额外判别价值
3. 早期停止场景下，相同token开销时减少采样链数的方案在MATH500上的准确率比DeepConf高1.6个百分点，所有置信度相关停止规则均无优势

**最值得记住的一句话**：任何基于token置信度的推理链优化都必须先和链长基线做对比，否则很可能是在为长度效应做无用的复杂封装。
