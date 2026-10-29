---
title: 'When Visual Evidence Is Insufficient: How Instructions, Post-Training, and
  Internal Activations Shape Refusal in Multimodal Language Models'
title_zh: 多模态大模型视觉证据不足场景下的拒绝行为控制机制研究
authors:
- Ananth K Suresh
- Aveen Dayal
- Gouthaman KV
- Aditya Pola
- Vineeth N Balasubramanian
affiliations:
- Indian Institute of Technology Hyderabad
arxiv_id: '2610.37430'
url: https://arxiv.org/abs/2610.37430
pdf_url: https://arxiv.org/pdf/2610.37430
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态大模型 · 拒绝行为控制
tags:
- MLLM
- Activation Steering
- Alignment
- Refusal Behavior
- Prompt Engineering
one_liner: 系统分析指令、后训练、内部激活三类因素对多模态大模型证据型拒绝行为的影响规律
practical_value: '- 电商多模态商品问答/客服Agent开发，可直接复用本文的细粒度拒绝分类框架，区分证据不足拒、安全拒、无理由拒三类行为，针对性优化策略，降低用户不满

  - 多模态Prompt工程可直接参考测试结论：证据感知拒答指令放在问题前缀（适配InternVL系列）或后缀（适配Qwen-VL系列），可提升18~45pct的证据不足拒绝率，减少幻觉输出

  - 低资源MLLM对齐场景优先选择SimPO做偏好训练，相比SFT/ORPO可降低10~30pct的“边拒绝边回答”混合响应率，输出行为更稳定，无明显性能损耗

  - 推理侧无需微调的拒答控制：可基于业务样本统计得到的拒绝激活方向做隐状态干预，可提升1~15pct的证据型拒绝率，不会造成正常请求误拒或性能下降'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
多模态大模型（MLLM）在电商商品问答、内容理解、智能客服等落地场景中，常遇到视觉证据不足无法回答的问题，若强行生成回复会引发严重幻觉，但现有评估仅关注整体拒绝率，无法区分模型是真识别到证据不足，还是触发安全过滤、无理由拒答，也未明确哪些因素可精准控制拒绝行为，导致拒答策略优化缺乏方向。

### 方法关键点
- 设计细粒度响应分类体系：定义尝试回答、证据型拒绝、安全型拒绝、无理由拒绝4类标签，新增混合响应（同时出现拒答和回答内容）标记，避免单一拒绝率的评估偏差
- 三类控制因子对照实验：① 指令层：测试4类响应政策（无额外指令、证据感知拒答、安全导向拒答、通用拒答）+2种放置位置（问题前缀/后缀）的影响；② 后训练层：对比SFT、DPO、ORPO、SimPO四种对齐方式对拒答行为的作用；③ 激活层：从天然拒答/回答样本的隐状态计算行为导向的拒绝方向，推理时通过隐状态偏移控制拒答
- 采用同一样本配对比较框架，所有对比固定图像-问题对，用Qwen3.5作为LLM裁判统一标注响应类型，消除样本差异干扰

### 关键结果
实验基于MoHoBench（900条视觉不可答问题），测试InternVL3-2B/8B、Qwen2.5-VL-7B三个主流开源MLLM：
- 指令层：证据感知/通用拒答指令可提升18.4~45.2pct总拒绝率，指令位置效果模型依赖（InternVL放前缀优，Qwen放后缀优），会导致13.7%~23.6%的样本改变拒答状态
- 后训练层：SFT/ORPO可将无指令场景的拒绝率提升至83.9%~94.9%，但混合响应率高达24.1%~33.2%；SimPO提升幅度小但混合响应率仅2.8%~7.9%，无无差别拒答问题
- 激活干预：单模型通用拒绝激活方向可跨指令条件提升1.1~15.1pct证据型拒绝率，无MMMU性能下降，也不会对良性图像描述请求产生误拒

### 核心结论
MLLM在视觉不可答场景的拒绝率本身不代表可靠性，必须结合拒绝原因、同样本行为跃迁、选择性控制三个维度评估，避免被聚合指标误导。
