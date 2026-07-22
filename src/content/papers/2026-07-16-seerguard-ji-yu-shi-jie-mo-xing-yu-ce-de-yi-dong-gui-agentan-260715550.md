---
title: 'SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction'
title_zh: SeerGuard：基于世界模型预测的移动GUI Agent安全防护框架
authors:
- Xue Yu
- Bo Yuan
- Pengshuai Yang
- Kailin Zhao
- Hong Hu
- Junlan Feng
affiliations:
- JIUTIAN Research
arxiv_id: '2607.15550'
url: https://arxiv.org/abs/2607.15550
pdf_url: https://arxiv.org/pdf/2607.15550
published: '2026-07-16'
collected: '2026-07-22'
category: Agent
direction: 移动GUI Agent 主动安全防护
tags:
- GUI Agent
- World Model
- Safety Guardrail
- VLM
- Multi-task Learning
one_liner: 结合指令级预筛查和世界模型动作级风险预判的移动GUI Agent主动安全方案
practical_value: '- 电商APP端智能助手（自动下单、账号管理类Agent）可直接复用双阶段安全架构：先拦截明确恶意指令，再预判动作语义后果，避免误扣款、隐私泄露等不可逆损失，比事后拦截方案更可靠

  - 业务Agent的动作预判模块可采用「语义级状态预测」替代像素级界面生成，大幅降低计算开销，满足在线低延迟部署要求

  - 安全防护模型冷启动时，可复用「通用安全文本+合成领域风险文本+小量真实多模态风险数据」的混合数据方案，无需收集大量违规操作的真实交互数据

  - 安全-效用平衡的评估指标SUS/RCS可直接复用在业务Agent的安全效果评估中，避免安全模块过度拦截正常请求影响用户体验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有移动GUI Agent的安全机制要么仅做指令级恶意检测，不感知实时GUI上下文，要么是执行后的事后校验，无法避免误操作导致的不可逆损失（如误支付、数据删除、隐私泄露），亟需能预判动作后果的主动安全能力。

### 方法关键点
- 双阶段级联架构：第一阶段指令级筛查优先拦截明确恶意请求，高召回低误拒，上下文相关的风险交给第二阶段处理，平衡安全与效用；第二阶段动作级风险评估基于当前GUI状态，预判候选动作的语义后果后再决定是否放行。
- 安全增强世界模型（SAWM）：基于Qwen3-VL-8B做SFT，多任务联合训练语义下一跳预测与安全风险评估，不生成像素级界面，仅输出功能层面的语义状态变化，算力开销低适配在线部署。
- 低资源数据增强方案：针对风险数据稀缺问题，混合三类数据训练：通用文本安全数据做基础安全对齐、多模态移动风险数据做领域适配、合成文本移动风险数据做跨模态桥接，整体正负样本比2:1，平衡安全检测能力与正常任务通过率。

### 关键实验
在MobileSafetyBench基准测试中，对接Qwen3-VL、GPT-5.1、Gemini-3.1三类Agent backbone，α=0.8时风险成本得分RCS分别下降62.5%、51.8%、51.1%；ω=0.8时Qwen3-VL的安全效用得分SUS从0.191提升至0.596；动作级风险评估在MobileRisk上F1达0.723，下一跳语义预测准确率达0.762，超过235B MoE模型的0.651。

**最值得记住的一句话**：Agent安全防护不能仅依赖指令筛查和事后校验，基于语义世界模型的动作后果预判是平衡安全、效用、部署成本的可行路径。
