---
title: 'Rethinking Video Agents: When and Why Video Harnesses Work'
title_zh: 视频Agent再思考：自适应观测工具链的生效条件与内在机制
authors:
- Luoyuan Zhang
- Xuanyu Zheng
- Yancheng Long
- Haoyang Xu
- Bin Wen
- Tingting Gao
affiliations:
- KlingAI Research
arxiv_id: '2611.31883'
url: https://arxiv.org/abs/2611.31883
pdf_url: https://arxiv.org/pdf/2611.31883
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: 视频Agent · 自适应观测机制优化
tags:
- VideoAgent
- Adaptive Observation
- Multimodal LLM
- Agentic Harness
- Video Understanding
one_liner: 提出自适应观测框架Video-Relook，明确视频Agent工具链收益的决定条件
practical_value: '- 电商短视频/直播内容理解场景可复用Video-Relook的分层观测逻辑：默认先做1fps全局粗排，仅对商品动作识别、违规内容检测等高细粒度需求任务，触发高帧率局部clip/空间裁剪工具，降低全量高清处理的计算成本

  - 多模态Agent工具调用链路可参考其置信度驱动的停止机制：给每轮工具调用增加"答案已确认无需更多观测"的出口，结合错误恢复率、回归率阈值动态停止交互，减少无效工具调用

  - 多模态模型选型时不能仅看单轮基准准确率，需同时评估模型的主动观测意愿、错误修正能力和正确答案留存率，避免高修正收益被高 regression 率抵消'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有视频理解普遍采用固定时空采样策略，容易遗漏细粒度关键视觉信息；引入Agentic Harness允许模型主动请求观测的范式虽有潜力，但缺乏对生效条件的系统性研究，无法明确何时、为何自适应观测能带来实际收益，也难以解释不同模型/任务下的增益差异。
### 方法关键点
- 搭建Video-Relook实验框架：从默认1fps全局概览出发，允许模型在最多3轮交互中调用clip/frames/montage/scan/overview共5类观测工具，自主选择观测的时间范围、帧率、空间裁剪区域，完成答案迭代
- 设计收益拆解指标：将准确率增益ΔA拆解为错误恢复率r（修正基准错误的比例）和正确答案回归率d（推翻基准正确答案的比例），同时区分初始轮prompt带来的增益和新增观测带来的增益
- 构建内部细粒度动作基准FastAct：覆盖体育、舞蹈、格斗等场景的100条视频共1000道选择题，重点测试短时接触、动作顺序、局部姿态等细粒度理解能力
### 关键结果
- 细粒度动作任务FastAct上，5款参测MLLM的准确率增益从3.0pp到14.2pp不等，Gemini 3.6 Flash增益最高达14.2pp；其中主动观测意愿低的Qwen 3.7 Flash 55.7%的问题在首轮就停止交互，回归率高达20.6%，增益仅3.0pp
- 公开基准Video-MME-v2上，Gemini 3.8 Flash、Qwen 3.8 Flash分别获得3.78pp、5.25pp的准确率提升，部分模型在TempCompass、Video-Holmes等任务上出现负增益
> 最值得记住的结论：视频Agent工具链的有效收益，本质是高信息密度观测机会与模型可靠交互修正能力的双向对齐，并非接入工具就一定能带来性能提升
