---
title: Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction
  Bidding
title_zh: 小参数推理模型在竞价出价场景的价值损失原因拆解与优化方案
authors:
- Mahbod Khaleti
- Seyed Reza Tavakoli
- Baran Hoseini
- Alireza Noori
- Amir Amini
- Koorosh Aslansefat
- Marjan Alirezaie
- Ali Habibnia
affiliations:
- Dataism Laboratory for Quantitative Finance
- Princeton University
- University of Hull
- Toronto Metropolitan University
- Virginia Tech
arxiv_id: '2611.34068'
url: https://arxiv.org/abs/2611.34068
pdf_url: https://arxiv.org/pdf/2611.34068
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: LLM Agent 竞价决策优化
tags:
- LLM Agent
- Auction Bidding
- Reasoning Model
- Ad Bidding
- Inference Optimization
one_liner: 拆解4-14B推理模型在竞价出价场景的价值损失成因，给出低开销优化与审计方案
practical_value: '- 推理型LLM Agent做高价值数值决策（广告出价、预算分配等）时，若单决策价值>1美分，不要设置过短的推理token cap，放开到4096
  token可让4-14B模型恢复91%-100%的最优解收益，token成本远低于收益损失。

  - 读取推理模型输出前必须等待模型输出end-of-thinking标记、关闭推理块，无需额外成本即可将Phi-mini这类模型的eBay场景收益恢复率从42%提升到84%，AuctionNet场景从24%提升到81%。

  - 上线LLM决策Agent时可叠加轻量trace审计：用规则解析推理过程中各选项的计算值，与最终输出对比，不一致的请求用确定性规则覆盖，768token场景下收益恢复率可提升到84%-100%，审计规则可跨市场无调优直接迁移。

  - 小推理模型做收益权衡决策时有固有bias：倾向选择赢率最高的最高出价而非期望收益最高的选项，高价值决策场景可针对性增加bias校验逻辑，避免7-17%的盈余损失。'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前广告平台、电商拍卖场景越来越多用推理LLM Agent做竞价出价，单决策价值最高可达上百美元，但小参数推理模型的决策价值损失原因不清晰，复杂竞价任务无ground truth难以定位问题，也没有低成本的通用优化方案。

### 方法关键点
- 构造有明确ground truth的简化竞价决策任务：输入私有价值、候选出价及对应赢率，输出期望收益最高的出价，最优解由精确计算器给出，可完全拆解损失来源。
- 测试6款4-14B开源推理模型：Phi-4-mini-reasoning、Qwen3-4B/8B/14B、DeepSeek-R1-Distill-Llama-8B、Granite-3.2-8B-Instruct。
- 损失拆解为4类：最优选项未计算、算术错误、推理被token cap截断、已算出最优选项但最终输出跳过。
- 验证两类无额外成本优化方案：关闭推理块后再读取答案、trace与最终输出不一致时用规则覆盖。

### 关键实验结果
- 测试数据集：216个eBay真实拍卖场景、216个AuctionNet广告竞价模拟场景。
- 768强制token下，模型仅能恢复42%-85%的最优解收益，错误出价会导致7-17%的盈余损失；损失中算术错误占比极低，5款模型不超过5%，仅Granite-8B为22%。
- 放开到4096token无强制cap后，5款模型恢复91%-100%的最优收益；关闭推理块再读答案将Phi-mini的eBay场景恢复率从42%提升到84%，AuctionNet从24%提升到81%。
- 轻量trace审计可将768token场景的收益恢复率提升到84%-100%，审计规则可跨市场无调优直接迁移生效。

### 最值得记住的一句话
小推理模型做数值决策的损失90%以上来自工程配置（token cap、读out方式）和最终决策bias，而非算术能力不足。
